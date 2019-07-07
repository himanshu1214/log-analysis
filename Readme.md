# About:
Log Analysis
# Project Description:

'''
This project tries to implement basic commands for Relational Database,  Python, SELECT and VIEW queries etc.
We used fictional database news as part of Full Stack Web Devlopment.
News database had three tables:
1. articles which has columns like author(F.Key), title, slug, lead, body, time, id
2. author which has columns like name, bio, id(P.Key)
3. log which has columns like path, ip, method, status, time, id(P.Key)

Further we created  different views to acheive our goals of this project:
FIRSTLY THESE VIEWS CAN BE CREATED in the following sequence:

## VIEW1:
aut_art view --->> CREATE OR REPLACE VIEW aut_art AS SELECT A.slug, A.author, \
B.name FROM articles AS A, authors AS B WHERE A.author = B.id;

## VIEW2:
date_tab view -->> CREATE OR REPLACE VIEW date_tab AS SELECT \
to_char(time, 'yyyy/mm/dd') date_part, status FROM log;
## VIEW3:
view_group_query -->> CREATE OR REPLACE VIEW group_tab AS SELECT \
count(*) as num, date_part, status FROM date_tab group by date_part, status;
## VIEW4:
view_percent_error_tab -->> CREATE OR REPLACE VIEW error_tab AS SELECT \
A.num/B.sum*100 error, A.date_part FROM (SELECT num, date_part FROM \group_tab \
WHERE status='404 NOT FOUND' order by date_part ASC) A, (SELECT sum(num), \
date_part FROM group_tab group by date_part order by date_part) B WHERE \
A.date_part=B.date_part order by error DESC;

Below is the sequence to steps taken to utilize these VIEWS and get the results:
## RESULT1:
GET POPULAR Articles
For acheiving we used select and join between log and articles and get the top articles and Views
## RESULT2:
GET POPULAR authors
For acheiving this result we created VIEW 1 as mentioned earlier.
Then we joined aut_art view table and log table and further queried to get the top authors and views.

## RESULT3:
GET date with more than 1% errors
For acheiving the results we made multiple views such as date_tab, view_group_query, view_percent_error_tab
Then we select the date and error from the view_percent_error_tab where error is more than 1%.

# Prerequisites:
Virtual Box: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
Vagrant: https://www.vagrantup.com/downloads.html
VM configuration: https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
or git clone  https://github.com/udacity/fullstack-nanodegree-vm
Data:
# SSH into Virtual Machine using vagrant:
Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

# Running PostgreSQL:
Inside the VM, change directory to /vagrant and look around with ls.
The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.
Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

# Logging In and Out
The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements:
f you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

# Download the data
Next, download the data here using (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql (). Put this file into the vagrant directory, which is shared with your virtual machine.
To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version/ https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840?contentVersion=1.0.0&contentLocale=en-us)

# Load Data
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Explore More data:
Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.

\dt — display tables — lists the tables that are available in the database.
\d table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

## Connecting from your code:
The database that you're working with in this project is running PostgreSQL. In your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

db = psycopg2.connect("dbname=news")

# RUN MODULE:
1. Module can be run on terminal using python temp.py and it will print the values of three questions in a form of Dataframe on terminal.

# ISSUES:
The news dataset used for this module is cleaned. No issues were encountered while implementing this module.

# LICENSE:
