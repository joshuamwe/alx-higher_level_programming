#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """
    Create a new Engine instance
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """
    Create a configured "Session" class
    """
    Session = sessionmaker(bind=engine)

    """
    Create a Session instance
    """
    session = Session()

    """
    Query the database and update the name of the state where id=2
    """
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = 'New Mexico'
        session.commit()

    """
    Close the session
    """
    session.close()
