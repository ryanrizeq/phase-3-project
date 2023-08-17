from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Dog, Kennel, Owner

engine = create_engine('sqlite:///doggy_daycare.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_dogs():
    pass
