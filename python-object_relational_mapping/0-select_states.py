#!/usr/bin/python3
"""
A Python script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to a MySQL database and lists all states from the database.
    """
    database = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=db_name,
        port=3306
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    database.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
