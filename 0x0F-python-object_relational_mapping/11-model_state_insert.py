#!/usr/bin/python3
# adds an State object to database


if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.engine.url import URL
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

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
