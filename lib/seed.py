from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import choice as rc

from models import Dog, Kennel, Owner

fake = Faker()

engine = create_engine('sqlite:///doggy_daycare.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Dog).delete()
session.query(Kennel).delete()
session.query(Owner).delete()

dogs = [Dog(
    name = fake.language_name(),
    breed = fake.job(),
    owner_id = fake.random_int(min=1, max=17)
) for i in range(20)]

kennel_sizes = ['Small', 'Medium', 'Large']
kennels = [Kennel(
    number = fake.random_int(min=1, max =20),
    size = rc(kennel_sizes),
    occupied_nights = fake.random_int(min=1, max=15),
    owner_id = fake.random_int(min=1, max=17)
) for i in range(20)]

owners = [Owner(
    first_name = fake.first_name(),
    last_name = fake.last_name()
) for i in range(17)]

session.add_all(dogs + kennels + owners)
session.commit()
