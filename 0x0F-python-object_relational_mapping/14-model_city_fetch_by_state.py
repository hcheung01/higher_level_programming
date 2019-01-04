#!/usr/bin/python3
""" prints all City objects from the database"""


if __name__ == "__main__":
    from sqlalchemy.engine import create_engine
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City
    from sys import argv

    db = {'drivername': 'mysql+mysqldb',
          'host': 'localhost',
          'port': '3306',
          'username': argv[1],
          'password': argv[2],
          'database': argv[3]}

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state, city in session.query(State, City)\
                              .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
