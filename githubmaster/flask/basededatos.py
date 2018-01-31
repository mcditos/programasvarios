
# coding: utf-8

# In[1]:

import sys


# In[2]:

from sqlalchemy import Column,ForeignKey,Integer,String, create_engine


# In[3]:

from sqlalchemy.ext.declarative import declarative_base


# In[4]:

from sqlalchemy.orm import relationship


# In[5]:

Base=declarative_base()


# In[6]:

class Restaurant(Base):
    __tablename__='restaurant'
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)
class MenuItem(Base):
    __tablename__='menu_item'
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)
    course=Column(String(250))
    description=Column(String(250))
    price=Column(String(8))
    restaurant_id=Column(Integer,ForeignKey('restaurant.id'))
    restaurant=relationship(Restaurant)


# In[7]:

engine=create_engine('sqlite:///restaurantmenu.db')


# In[8]:

Base.metadata.create_all(engine)

