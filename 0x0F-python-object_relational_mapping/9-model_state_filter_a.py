#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from
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

    """
    Create engine and connect to the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, mysql_db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query the database for all State objects containing 'a'
    """
    states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    """Print the results
    """
    for state in states:
        print("{}: {}".format(state.id, state.name))
