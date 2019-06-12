#!/usr/bin/env python2

import psycopg2

DBNAME = "news"

question_one = "1. What are the most popular three articles of all time?"
query_one = """
SELECT title, COUNT(*) AS views FROM articles
INNER JOIN log
ON articles.slug = SUBSTRING(log.path, 10)
WHERE log.status LIKE '%200%'
GROUP BY articles.title
ORDER BY views DESC LIMIT 3;
"""

question_two = "2. Who are the most popular article authors of all time?"
query_two = """
SELECT authors.name, COUNT(*) AS views FROM articles
INNER JOIN authors
ON articles.author = authors.id
INNER JOIN log
ON articles.slug = SUBSTRING(log.path, 10)
GROUP BY authors.name
ORDER BY views DESC LIMIT 4;
"""

question_three = "3. On which more than 1 percent of requests lead to errors?"
query_three = """
SELECT error_logs.date, round(100.0 * error / total, 2) AS percent
FROM total_logs
INNER JOIN error_logs
ON total_logs.date = error_logs.date
WHERE error > total / 100;
"""


def connect_db(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data


def popular_articles():
    data = connect_db(query_one)

    print question_one
    for i in range(len(data)):
        print "\n"
        print "\"" + data[i][0] + "\" - " + str(data[i][1]) + " views"
    print "\n"


def popular_authors():
    data = connect_db(query_two)

    print question_two
    for i in range(len(data)):
        print "\n"
        print "\"" + data[i][0] + "\" - " + str(data[i][1]) + " views"
    print "\n"


def error_status():
    data = connect_db(query_three)

    print question_three
    for i in range(len(data)):
        print "\n"
        print str(data[i][0]) + " - " + str(data[i][1]) + " %" + " errors"
    print "\n"


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    error_status()
