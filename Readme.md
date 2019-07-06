'''The function of this module is to connect the news database
from psql get the popular articles, popular author, date when the more than 1% error occured'''

1. The main Class Articles consist of three main function like get-get_popular_articles, get_popular_author_name, get_request_errors
which prints the popular articles, author names, %percent errors.
2. Module can be run on terminal using python temp.py and it will print the values of three questions in a form of Dataframe on terminal.
3. For getting popular authors created VIEW as aut_art ,"CREATE OR REPLACE VIEW aut_art AS SELECT A.slug, A.author, B.name FROM articles AS A, authors AS B WHERE A.author=B.id;"
4. For getting top % errors ,creared multiple VIEWS as view_date_tab
"CREATE OR REPLACE VIEW date_tab AS SELECT date_part('day', time), status FROM log;"
VIEW2 : view_group_query: "CREATE OR REPLACE VIEW group_tab AS SELECT count(*) as num, date_part, status FROM date_tab group by date_part, status;"
VIEW3: view_percent_error_tab:'CREATE OR REPLACE VIEW error_tab AS SELECT A.num/B.sum*100 error, A.date_part \
    FROM (SELECT num, date_part FROM group_tab WHERE status='404 NOT FOUND' order by date_part ASC) A, \
    (SELECT sum(num), date_part FROM group_tab group by date_part order by date_part) B WHERE A.date_part=B.date_part order by error DESC;'
