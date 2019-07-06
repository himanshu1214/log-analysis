# Log Analysis
### Full Stack Web Development

## About

'''The module shows the basic understanding of python, relational databases, queries, views etc.
As part of the Full Stack Web Developer course, we got a fictional news database, which consist of
three tables articles, author, log.
# 1. Articles - author(F.Key), title, slug, lead, body, time, id.
# 2. Authors - name, bio, id(P.Key).
# 3. log - path, ip, method, status, time, id

Following are the results acheived :
# 1. popular articles
# 2. popular author
# 3. date when more than 1% error occured in ststus of log tables

Following are methods:
Created a class Articles which consisted of three functions to get the desired results.
## 1. For getting popular Articles - created get_popular_articles function which uses a select query ,join between
author and logs to get the results for top 3 articles.
## 2. For getting popular get_popular_author_name - created a view by joining two article and authors names as aut_art
further joined log table with aut_art and querying it get the top 3 authors.
#VIEW
"CREATE OR REPLACE VIEW aut_art AS SELECT A.slug, A.author, B.name FROM articles AS A, authors AS B WHERE A.author=B.id;"
## 3. For getting get_request_errors - created date_tab view by selecting date,status from log.
created group_query view by grouping date and status, further created percent_error_tab View by dividing two select
queries. Finally used a select query to get the date when the error is more than 1%.
# VIEW2 : view_group_query:
"CREATE OR REPLACE VIEW group_tab AS SELECT count(*) as num, date_part, status FROM date_tab group by date_part, status;"

# VIEW3: view_percent_error_tab:
CREATE OR REPLACE VIEW error_tab AS SELECT A.num/B.sum*100 error, A.date_part FROM (SELECT num, date_part FROM group_tab WHERE status='404 NOT FOUND' order by date_part ASC) A, (SELECT sum(num), date_part FROM group_tab group by date_part order by date_part) B WHERE A.date_part=B.date_part order by error DESC;

## Run module:
#1. Module can be run on terminal using python temp.py and it will print the values of three questions in a form of Dataframe on terminal.
#2. For getting popular authors created VIEW as aut_art ,
#4. For getting top % errors ,creared multiple VIEWS as view_date_tab
"CREATE OR REPLACE VIEW date_tab AS SELECT date_part('day', time), status FROM log;"

'''
## Prerequisites:
# Python2 : https://www.python.org/downloads/release/python-2715/
# Virtual Box : https://www.virtualbox.org/wiki/Downloads
# Vagrant :https://www.vagrantup.com/
## Get and Set the news database :
Download the data: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
Next, You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840?contentVersion=1.0.0&contentLocale=en-us)

To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## SSH into vagrant:
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
