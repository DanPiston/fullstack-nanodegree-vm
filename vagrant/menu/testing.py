from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

all_rest = session.query(Restaurant).all()
for y in all_rest:
    print(y.name)

just_right = session.query(Restaurant).filter_by(name="Not Really A Test").delete()
session.commit()
