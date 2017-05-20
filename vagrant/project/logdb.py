#!/usr/bin/env python3

# Database log project for Udacity
import psycopg2
from pprint import pprint
DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)

def get_top_three():
    """Returns list of paths and visits for top 4
       most visited articles"""
    c = db.cursor()
    query = """
           select art_paths.title, count(log.path) as count
           from art_paths join log
           on art_paths.path = log.path
           group by art_paths.title
           order by count desc
           limit 3;
           """
    c.execute(query)
    top_list = c.fetchall()
    c.close()
    print('The Top 3 Articles:')
    for entry in top_list:
        print('{} --- {} views'.format(entry[0], entry[1]))


# TODO Who are the most popular article authors of all time?
def get_author_info():
    """Return article slug and author"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
            select articles.slug, authors.name
            from articles join authors
            on articles.author = authors.id;
            """
    c.execute(query)
    author_info = c.fetchall()
    db.close()
    for x in author_info:
        print(x[0])


# TODO Which days did more than 1% of requests lead to errors?


get_top_three()
#top_three_solution(get_top_three())
#get_author_info()
