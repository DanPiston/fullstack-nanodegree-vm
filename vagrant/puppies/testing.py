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


3. Query all puppies by ascending weight

4. Query all puppies grouped by the shelter in which they are staying
'''
#1. Query all of the puppies and return the results in ascending alphabetical order
def all_pups():
    all_puppies = session.query(Puppy).order_by(Puppy.name).all()
    for pup in all_puppies:
        print(pup.name)

#2. Query all of the puppies that are less than 6 months old organized by the youngest first
young_pups = session.query(Puppy).order_by(desc(Puppy.dateOfBirth)).all()
six_months = datetime.strftime((datetime.now() - timedelta(days = 180)), "%b")
print(six_months)


#spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
#print(spinach.restaurant.name)
#session.delete(spinach)
##session.commit()
#spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
