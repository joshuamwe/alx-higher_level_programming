#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    Create connection
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """
    Create a configured "Session" class
    """
    Session = sessionmaker(bind=engine)

    """
    Create a Session
    """
    session = Session()

    """
    Add new state
    """
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """
    Print new state id
    """
    print(new_state.id)
