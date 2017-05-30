from datetime import datetime, timedelta

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

'''
Using SQLAlchemy perform the following queries on your database:



'''
#1. Query all of the puppies and return the results in ascending alphabetical order
def all_pups():
    all_puppies = session.query(Puppy).order_by(Puppy.name).all()
    for pup in all_puppies:
        print(pup.name)

#2. Query all of the puppies that are less than 6 months old organized by the youngest first
def pup_age():
    young_pups = session.query(Puppy).order_by(desc(Puppy.dateOfBirth)).all()
    six_months = datetime.utcnow() - timedelta(days=180)
    young_pups = session.query(Puppy).filter(Puppy.dateOfBirth < six_months).all()
    for pup in young_pups:
        print('{} born {}'.format(pup.name, pup.dateOfBirth))

#3. Query all puppies by ascending weight
def pup_weight():
    all_puppies = session.query(Puppy).order_by(Puppy.weight).all()
    for pup in all_puppies:
        print(pup.weight)

#4. Query all puppies grouped by the shelter in which they are staying
def pup_by_shelter():
    pup_shelter = session.query(
                    Puppy, Shelter
                    ).join(Shelter
                    ).order_by(Shelter.name
                    ).all()
    for pup in pup_shelter:
        print('{} is at {}'.format(pup.Puppy.name,pup.Shelter.name))

pup_by_shelter()
