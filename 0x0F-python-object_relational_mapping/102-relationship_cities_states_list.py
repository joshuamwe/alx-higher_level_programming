#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
    Query the database to get all City objects, sorted by ID
    """
    cities = session.query(City).order_by(City.id).all()

    """
    Print the results in the required format
    """
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
