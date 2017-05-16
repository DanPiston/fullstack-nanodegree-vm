#Database log project for Udacity
import psycopg2
from pprint import pprint

DBNAME = 'news'

def get_top_three():
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    query = """
            select path, count(path) as count
            from log
            group by path
            order by count desc
            limit 4;
            """
    c.execute(query)
    data = c.fetchall()
    db.close()
    for entry in data:
        print("The article {} had {} visits".format(entry[0], entry[1]))

get_top_three()
