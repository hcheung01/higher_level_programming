#!/usr/bin/python3
# print first state objects from the database

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.engine.url import URL

    # url
    url = {'drivername': 'mysql+mysqldb',
           'host': 'localhost',
           'port': '3306',
           'username': argv[1],
           'password': argv[2],
           'database': argv[3]}

    c_url = URL(**url)

    # create engine, metadata for stored objects
    engine = create_engine(c_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # session
    session = Session(engine)

    try:
        first = session.query(State).first()
        print("{}: {}".format(first.id, first.name))
    except:
        print('Nothing')

    # close
    session.close()
