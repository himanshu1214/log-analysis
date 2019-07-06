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
        self.conn.execute("SELECT count(*) as views, title FROM log JOIN articles ON log.path = concat('/article/', articles.slug) group by title order by views DESC LIMIT 3;")
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
        self.conn.execute("SELECT A.name, count(*) as views FROM aut_art A \
        INNER JOIN log AS B ON B.path = concat('/article/', A.slug) group by A.name \
        order by views DESC LIMIT 3;")
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
        select_query = 'SELECT * FROM error_tab WHERE error>1;'
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
