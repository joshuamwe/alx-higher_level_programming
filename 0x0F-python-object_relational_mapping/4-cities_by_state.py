#!/usr/bin/python3
"""
Script that lists all cities from database 'hbtn_0e_4_usa'
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Get values for mysql username, password and database
    name from the command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database = sys.argv[3]

    """
    Connect Mysql server
    """
    mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database)

    """
    Create a cursor object to execute queries
    """
    cursor = mydb.cursor()

    """
    Execute SELECT query to list all cities from the
    database
    """
    query = "SELECT c.id, c.name, s.name\
                FROM cities as c\
                INNER JOIN states as s\
                ON c.state_id = s.id\
                ORDER BY c.id"
    cursor.execute(query)

    """
    Fetch all rows from result set
    """
    results = cursor.fetchall()

    """
    Display the results
    """
    for result in results:
        print(result)
