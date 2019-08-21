# Udacity-News-Log-Analysis

## About
This project will present the following results from a database.

1. Present most popular three articles
2. Present most popular article authors
3. Show for which day(s) more than 1% of requests led to errors

## Prerequisites

The log_analysis.py file runs on Python 2. Python can be downloaded from:
```
https://www.python.org/donwloads
```
The program executes within a Virtual Machine (VirtualBox). VirtualBox can be downloaded from:
```
https://www.virtualbox.org/wiki/downloads
```
The environment used to test the program was Vagrant. Vagrant can be downloaded from:
```
https://www.vagrantup.com/downloads.html
```
The project uses Postgres to query the database. To install run the following in your virtual environment:

sudo apt-get install postgresql

Python also requires psycopg2 as a package. To install psycopg2 run the following in the VM's terminal:

sudo pip install psycopg2

The project utilized the database *news* which can be downloaded from the following path:
```
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```
The content should be located within the vagrant directory shared between your computer and the VM

## Installation

In your vagrant directory run `vagrant up` and then `vagrant ssh`. Once in the vagrant directory, where the *newsdata.sql* file is located run the following:
```
psql -d news -f newsdata.sql
```
The database *news* should be accessible and the program ready to run.

## Views

Views were utilized to obtain the results from item 3 in the lest in the *About* section above. These views have to be created directly in the Postresql database before running of the log_analysis.py code.

To create the views connect to the database by typing `psql -d news` and running the following queries:

### View 1: errorcount
```
Create view errorcount as select date(time) as day, count(*) from log
where status !='200 OK' group by day;
```

### View 2: entrycount
```
Create view entrycount as select date(time) as day, count(*) from log group by day;
```

## Run Script
To run the log_analysis.py code, type the following in the command within the VM:
```
python log_analysis.py
```
Thank you.
