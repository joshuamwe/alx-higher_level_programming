#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where names matches the argument

Usage: ./3-my_safe_filter_states.py <username>
                                    <password>
                                    <database name>
                                    <state name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Taking arguments from the command line to create
    mysql username, password, database name and state to
    search for
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """
    Connecting to MySQL server
    """
    mydb = MySQLdb.connect(
            host='localhost',
            port=3305,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name)

    """
    Creating a cursor object to execute queries
    """
    cursor = mydb.cursor()

    """
    Execute a SELECT query to get the searched state from
    the database
    """
    query = "SELECT * FROM states ORDER BY id"
    cursor.execute(query)

    """
    Fetch all rows from the result set
    """
    results = cursor.fetchall()

    """
    Display the results
    """
    for result in results:
        if (result[1] == sys.argv[4]):
            print(result)
