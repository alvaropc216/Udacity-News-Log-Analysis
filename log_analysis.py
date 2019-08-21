#!/usr/bin/env python2

import psycopg2
DATABASE = "news"


def question1():

    db = psycopg2.connect(dbname=DATABASE)
    c = db.cursor()
    c.execute("Select articles.title, count(*) as num \
               from articles, (select substring (log.path from 10) \
                              as nickname \
                              from log where path != '/' and status ='200 OK')\
                              as shortlog \
               where articles.slug = shortlog.nickname \
               group by articles.title \
               order by num desc \
               limit 3;")
    results = c.fetchall()
    c.close()
    return results


def question2():
    db = psycopg2.connect(dbname=DATABASE)
    c = db.cursor()
    c.execute("Select authors.name, count(*) as num \
                from articles, authors, (select substring(log.path from 10)\
                as nickname \
                from log where path != '/' and status ='200 OK') as shortlog \
                where articles.slug = shortlog.nickname \
                and articles.author = authors.id \
                group by authors.name \
                order by num desc;")
    results = c.fetchall()
    c.close()
    return results


def question3():
    db = psycopg2.connect(dbname=DATABASE)
    c = db.cursor()
    c. execute("Select entrycount.day as day,\
                errorcount.count *100.0 / entrycount.count as ratio \
                from entrycount, errorcount \
                where entrycount.day = errorcount.day \
                and errorcount.count * 100.0 / entrycount.count >1.0;")
    results = c.fetchall()
    c.close()
    return results


if __name__ == '__main__':
    print("Question One:\n\
    What are the most popular three articles of all time?\n")
    result = question1()

    for i in result:
        print("'{}' - {} views".format(i[0], i[1]))

    print("\nQuestion Two:\n\
    Who are the most popular article authors of all time?\n")
    result2 = question2()

    for i in result2:
        print("{} - {} views".format(i[0], i[1]))

    print("\nQuestion Three:\n\
    On which days did more than 1% of requests lead to errors?\n")
    results3 = question3()

    for i in results3:
        print("{} - {}% errors".format(i[0], round(i[1], 1)))
