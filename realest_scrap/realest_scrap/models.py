from sqlalchemy import URL, Column, Engine, Integer, String, create_engine, BigInteger
from sqlalchemy.orm import declarative_base


DeclarativeBase = declarative_base()


def db_connect(database_url: URL) -> Engine:
    return create_engine(database_url)


def setup_tables(db_engine: Engine):
    DeclarativeBase.metadata.create_all(db_engine)


class Posting(DeclarativeBase):
    __tablename__ = 'postings'

    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String)
    location = Column('location', String)
    image_link = Column('image_link', String)
    insertion_order = Column('insertion_order', Integer)
