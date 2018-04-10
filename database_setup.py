from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

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
            'id'      : self.id,
            'name'    : self.name,
            'email'   : self.email,
            'picture' : self.picture
        }

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))

    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id'    : self.id,
            'name'  : self.name
        }

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250))

    category_name = Column(String(250), ForeignKey('category.name'))
    category = relationship(Category)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id'          : self.id,
            'title'       : self.title,
            'category'    : self.category_name,
            'description' : self.description,
            'user_id'     : self.user_id
        }

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)