from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

class Kennel(Base):
    __tablename__ = 'kennels'

    id = Column(Integer(), primary_key=True)
    number = Column(Integer())
    size = Column(String())
    occupied_nights = Column(Integer())

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())