#!/usr/bin/python3
"""List all states from a given db sorted in ascending order by id
Username, password, and database names are given as user args
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute('SELECT *FROM states\
               WHERE name LIKE BINARY "N%"\
               ORDER BY states.id ASC;')
    allStates = cur.fetchall()

    for state in allStates:
        print(state)

    cur.close()
    db.close()
