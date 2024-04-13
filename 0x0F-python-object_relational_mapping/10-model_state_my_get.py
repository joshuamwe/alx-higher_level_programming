#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Get command line arguments
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    Create engine and connect to the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, mysql_db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query the database for the State object with the specified name
    """
    state = session.query(State).filter_by(name=state_name).first()

    """
    Print the result
    """
    if state is None:
        print("Not found")
    else:
        print(state.id)
