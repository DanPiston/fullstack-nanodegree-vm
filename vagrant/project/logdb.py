#!/usr/bin/env python3

# Database log project for Udacity
import psycopg2
from pprint import pprint
DBNAME = 'news'


def get_top_three():
    """Returns list of paths and visits for top 4
       most visited articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
            select path, count(path) as count
            from log
            group by path
            order by count desc
            limit 4;
            """
    c.execute(query)
    top_three_list = c.fetchall()
    db.close()
    return top_three_list


def top_three_solution(path_list):
    """Prints out answer to what are the top three most visited articles."""
    titles = []
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print("The Top 3 Articles:")
    for x in path_list:
        query = """
                select title
                from articles
                where slug
                like '{}';
                """.format(x[0][9:])
        c.execute(query)
        title = c.fetchone()
        # Skips over '/' which is the most hit non-article
        if title:
            print("{} --- {} views".format(title[0], x[1]))
            titles.append(title)

# TODO Who are the most popular article authors of all time?
def get_author_info():
    """Return article slug and author"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
            select articles.slug, authors.name
            from articles
            join authors
            on articles.author = authors.id;
            """
    c.execute(query)
    author_info = c.fetchall()
    db.close()
    for x in author_info:
        print(x[0])


# TODO Which days did more than 1% of requests lead to errors?


#top_three_solution(get_top_three())
get_author_info()
