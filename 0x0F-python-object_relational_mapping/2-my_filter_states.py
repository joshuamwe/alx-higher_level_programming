#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument
Usage: ./2-my_filter_states.py <username>
                               <password>
                               <database name>
                               <state name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Get mysql username, password, database name and state
    name searched from command line arguments
    """
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_database = sys.argv[3]
    state_name = sys.argv[4]

    """
    Connect to MySQL server
    """
    mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_database)

    """
    Create cursor object to execute queries
    """
    cursor = mydb.cursor()

    """
    Execute a SELECT query that selects the searched state
    name
    """
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    """
    Fetch all the rows from the result set
    """
    results = cursor.fetchall()

    """
    Display the results
    """
    for result in results:
        print(result)
