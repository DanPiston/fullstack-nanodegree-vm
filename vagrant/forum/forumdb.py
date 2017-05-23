#!/usr/bin/env/ python3

# "Database code" for the DB Forum.
import psycopg2
import datetime
import bleach

DBNAME = "forum"

def get_posts():
    """Return all posts"""
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    query = "select content, time from posts order by time desc"
    c.execute(query)
    return c.fetchall()
    db.close()

def add_post(content):
    clean_content = bleach.clean(content)
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    c.execute("insert into posts values (%s)", (clean_content,))
    db.commit()
    db.close()
