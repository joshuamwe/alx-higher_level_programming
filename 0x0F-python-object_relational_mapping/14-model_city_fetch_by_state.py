#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    """
    Set up connection to the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query the database for all states containing the letter 'a'
    """
    cities = session.query(City, State).filter(City.state_id == State.id).\
        order_by(City.id).all()
    """
    Print results
    """
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
