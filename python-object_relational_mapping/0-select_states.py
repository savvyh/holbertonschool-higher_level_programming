#!/usr/bin/python3
"""
A Python script that lists all states from the database hbtn_0e_0_usa.
Script takes 3 arguments: mysql username, mysql password, and database name.
Script uses the MySQLdb module to connect to a MySQL server
running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to a MySQL database and lists all states from the database.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:  # Ensuring there are three arguments
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
