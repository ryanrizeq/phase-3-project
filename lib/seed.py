from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Dog, Kennel, Owner

fake = Faker()

engine = create_engine('sqlite:///doggy_daycare.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_data():
    dogs = [Dog(
        name = fake.language_name(),
        breed = fake.animal.dog()
    ) for i in range(20)]

    session.add_all(dogs)
    session.commit()
