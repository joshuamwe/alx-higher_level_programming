#!/usr/bin/python3
"""
Adds the State object “California” with the City “San Francisco”
to the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    """
    Get MySQL credentials
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """
    Create engine and link to database
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(mysql_username, mysql_password, database_name),
        pool_pre_ping=True)

    """
    Create all tables in the engine
    """
    Base.metadata.create_all(engine)

    """
    Create session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Create California State object
    """
    california = State(name="California")

    """
    Create San Francisco City object and link it to California
    """
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    """
    Add California and San Francisco to session
    and commit changes
    """
    session.add(california)
    session.add(san_francisco)
    session.commit()
