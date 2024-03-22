#!/usr/bin/python3
"""
A Python script that lists all states from the database hbtn_0e_0_usa.
Script takes 3 arguments: mysql username, mysql password, and database name.
Script uses the MySQLdb module to connect to a MySQL server
running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
