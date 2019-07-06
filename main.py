#!/usr/bin/env python

import psycopg2
import pandas as pd

'''The function of this module is to connect the news
database from psql get the popular articles, popular
author, date when the more than 1% error occured'''


class Articles:
    def __init__(self):
        try:
            self.db = psycopg2.connect(database = 'news')
        except psycopg2.Err as e:
            print('Unable to connect to database')
            print(e.pgerror)
            print(e.diag.message_detail)
            sys.exit(1)

        self.conn=self.db.cursor()

#   Popular Articles:
    def get_popular_articles(self):
        '''
        gets popular articles and views from news database
        :param: takes no parameter
        :return: df: DataFrame of views and Articles
        '''
        self.conn.execute("SELECT count(*) as num, A.slug FROM articles AS A \
        INNER JOIN log AS B ON B.path like '%'|| A.slug || '%' group by A.slug \
        order by num DESC LIMIT 3;")
        res = self.conn.fetchall()
        df = pd.DataFrame(res, columns = ['Views', 'Articles'])
        # print(res)
        return df


# Popular Articles

    def get_popular_author_name(self):
        '''
        Fucntion returns the popular author names
        :param: takes no parameter
        :return: df: Dataframe of Author and Views
        '''
        self.conn.execute("CREATE OR REPLACE VIEW aut_art AS SELECT A.slug, \
        A.author, B.name FROM articles AS A, authors AS B WHERE A.author = B.id;")
        self.conn.execute("SELECT A.name, count(*) as num FROM aut_art A \
        INNER JOIN log AS B ON B.path like '%'|| A.slug || '%' group by A.name \
        order by num DESC LIMIT 3;")
        res = self.conn.fetchall()
        df = pd.DataFrame(res, columns = ['Author', 'Views'])
        return df

#Top request error

    def get_request_errors(self):
        '''
        This function returns the date where error more than 1% percent
        occured out of total requrest GET request sent
        :param: takes no parameter
        :return: df: Dataframe of %errors and Date
        '''
        view_date_tab = "CREATE OR REPLACE VIEW date_tab AS SELECT \
        to_char(time, 'yyyy/mm/dd') date_part, status FROM log;"
        view_group_query = 'CREATE OR REPLACE VIEW group_tab AS SELECT \
        count(*) as num, date_part, status FROM date_tab group by date_part, status;'
        view_percent_error_tab = "CREATE OR REPLACE VIEW error_tab AS SELECT \
        A.num/B.sum*100 error, A.date_part FROM (SELECT num, date_part FROM \
        group_tab WHERE status='404 NOT FOUND' order by date_part ASC) A, \
        (SELECT sum(num), date_part FROM group_tab group by date_part \
        order by date_part) B WHERE A.date_part=B.date_part order by error DESC;"
        select_query = 'SELECT * FROM error_tab WHERE error>1;'
        self.conn.execute(view_date_tab)
        self.conn.execute(view_group_query)
        self.conn.execute(view_percent_error_tab)
        self.conn.execute(select_query)
        res = self.conn.fetchall()
        df=pd.DataFrame(res, columns=['%error', 'date'])
        return df

    def __str__(self):

        return 'Poular Articles: \n {} \n , Popular Authors: \n {}, \n Date with more than onePercenterror: \n {}'\
        .format(self.get_popular_articles(), self.get_popular_author_name(), \
        self.get_request_errors())
if __name__ == '__main__':
    articles= Articles()
    print(articles)
    articles.db.close()
