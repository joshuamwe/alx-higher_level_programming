#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """
    Set up connection to the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query the database for all states containing the letter 'a'
    """
    states = session.query(State).filter(State.name.like('%a%')).all()

    """
    Delete each state object found
    """
    for state in states:
        session.delete(state)

    """
    Commit changes and close session
    """
    session.commit()
    session.close()
