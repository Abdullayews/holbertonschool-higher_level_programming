#!/usr/bin/python3
"""Displays all values in states table where name matches argument, SQL injection safe"""
import MySQLdb
import sys


def filter_states():
    """Takes arguments argv to list from database
    Safe from MySQL injection using parameterized queries
    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s \
                ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
