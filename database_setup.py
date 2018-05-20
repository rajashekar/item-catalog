from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import datetime

Base = declarative_base()


# User model to hold user details
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250))
    picture = Column(String(250))

    @property
    def serialize(self):
        """ Return Object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture
        }


# Category model to hold category details
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))

    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id': self.id,
            'name': self.name
        }


# Item model to hold item details
class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250))
    modified_date = Column(DateTime, default=datetime.datetime.utcnow)

    category_name = Column(String(250), ForeignKey('category.name'))
    category = relationship(Category)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category_name,
            'description': self.description,
            'modified_date': self.modified_date,
            'user_id': self.user_id
        }


engine = create_engine('sqlite:////var/www/html/item-catalog/itemcatalog.db')
Base.metadata.create_all(engine)
