#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Getting values for mysql username, passwordm and
    database name from command line arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """
    Connecting to MySQL server
    """
    mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database)

    """
    Creating a cursor object to execute queries
    """
    cursor = mydb.cursor()

    """
    Execute a SELECT query that selects the state name
    searched for
    """
    query = "SELECT *\
                FROM cities c\
                INNER JOIN states s\
                ON c.state_id = s.id\
                ORDER BY c.id"
    cursor.execute(query)

    """
    Fetch all row in the result set
    """
    results = cursor.fetchall()

    """
    Display results
    """
    print(", ".join(
        [result[2] for result in results if result[4] == sys.argv[4]]))
