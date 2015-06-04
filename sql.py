# sql.py - Create a SQLite3 table and populate it with data


import sqlite3


# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()
    # create the table
    c.execute("DROP TABLE if exists posts")
    c.execute(""" CREATE TABLE posts(title TEXT, post TEXT)""")
    # insert dummy data into the table
    c.execute('INSERT INTO posts values("Good","I\'m good")')
    c.execute('INSERT INTO posts values("Well","I\'m well")')
    c.execute('INSERT INTO posts values("Excellent","I\'m excellent")')
    c.execute('INSERT INTO posts values("Nice","I\'m nice")')
    c.execute('INSERT INTO posts values("Okay","I\'m okay")')
    c.execute('INSERT INTO posts values("Cool","I\'m cool")')
