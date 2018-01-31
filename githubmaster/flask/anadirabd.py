
# coding: utf-8

# In[2]:


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basededatos import Base, Restaurant, MenuItem


# In[6]:


engine=create_engine('sqlite:///restaurantmenu.db')


# In[7]:


Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)


# In[8]:


Session=DBsession()


# In[21]:


r1=Restaurant(name="Toma huevo mardito")
r2=Restaurant(name="sarchicha Porlacu KA")
r3=Restaurant(name="La Casa del Marico")
r4=Restaurant(name="Quejeso we")
Session.add(r1)
Session.add(r2)
Session.add(r3)
Session.add(r4)


# In[23]:


Session.query(Restaurant).all()


# In[24]:


plato1=MenuItem(name="Chorizo portuano",description="Tu sabeeeee",course="SEXO CANDENTE",                price="Barato para ti",restaurant=r2)
plato2=MenuItem(name="Transtijera",description="descubrelo bebe",course="SEXO CANDENTE",                price="Barato para ti",restaurant=r1)
plato3=MenuItem(name="er chikigloti",description="gordito sabroson",course="SEXO CANDENTE",                price="Barato para ti",restaurant=r3)
plato4=MenuItem(name="randy.parraga.esgay.com.ve",description="Todo lo que neptuno salvaje de ofrece",course="Me dicen lukaku",                price="para ti gratis mi amor",restaurant=r4)


# In[25]:


Session.add(plato1)
Session.add(plato2)
Session.add(plato3)
Session.add(plato4)


# In[26]:


Session.commit()
Session.query(MenuItem).all()


# In[27]:


Session.query(Restaurant).all()


# In[39]:





# In[49]:





# In[50]:




