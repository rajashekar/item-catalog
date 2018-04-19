from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Category, Item, Base

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

# Create dummy category
category1 = Category(name="TV")
session.add(category1)
session.commit()

category2 = Category(name="Gaming Console")
session.add(category2)
session.commit()

# Create dummy items
item1 = Item(user_id=1, title="Samsung TV",
             description="Samsung TV 55 inch 4K",
             category_name="TV")
session.add(item1)
session.commit()

item2 = Item(user_id=1, title="LG TV",
             description="LG TV 55 inch 4K",
             category_name="TV")
session.add(item2)
session.commit()

item3 = Item(user_id=1, title="Sony playstation 4",
             description="Console game by Sony",
             category_name="Gaming Console")
session.add(item3)
session.commit()

item4 = Item(user_id=1, title="Xbox one",
             description="Console game by Microsoft",
             category_name="Gaming Console")
session.add(item4)
session.commit()

item5 = Item(user_id=1, title="Nintendo",
             description="Console game by Nintendo",
             category_name="Gaming Console")
session.add(item5)
session.commit()

print "added sample items"
