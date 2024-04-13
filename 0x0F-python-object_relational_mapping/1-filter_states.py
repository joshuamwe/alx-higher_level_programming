#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from database 'hbtn_0e_0_usa'
Usage: ./1-filter_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Get mysql username, password and database name
    from command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """
    Connect to MySQL server
    """
    mydb = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_username,
            password=mysql_password,
            db=database_name)

    """
    Create a cursor object to execute queries
    """
    cursor = mydb.cursor()

    """
    Execute a SELECT query to get all the states starting with 'N'
    from the database
    """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """
    Fetch all the rows from the result set
    """
    results = cursor.fetchall()

    """
    Display results
    """
    for result in results:
        if (result[1][0] == 'N'):
            print(result)
