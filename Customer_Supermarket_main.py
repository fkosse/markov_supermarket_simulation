#!/usr/bin/env python
# coding: utf-8

# In[200]:


import random 
import pandas as pd
import numpy as np


# In[201]:


mx=pd.read_csv('mx.csv')
mx=mx.set_index('before')
mx


# In[336]:


# states\locations
mx.columns.values


# In[544]:


# What are the transition probabilities if the current state is fruit
mx['fruit'][0]


# In[602]:


class Customer:
    """
    a single customer that moves through the supermarket in a MCMC simulation """
    
    def __init__(self, id):
        self.id=id
        self.location='entrance'
        self.transition_probs=mx

    def __repr__(self):
        return f'Customer {self.id} is in {self.location}'
    
    def next_state(self):
        ''' Propagates the customer to the next state. Returns nothing.   '''
        self.location = np.random.choice(self.transition_probs.columns.values, p=self.transition_probs.loc[self.location])
    
    def is_active(self):
        """ Returns True if the customer has not reached the checkout yet. """
        if self.location=='checkout':
            return False
        else:
            return True


# In[603]:


class Supermarket:
    """manages multiple Customer instances that are currently in the market.    """
    
    def __init__(self):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        
    def __repr__(self):
        return ''
    
    def get_time(self):
        """current time in HH:MM format,
        """
        return None
    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        return None

    def next_minute(self): #control our customers
        """propagates all customers to the next state."""
        for shopper in self.customers:
            shopper.next_state()
        
    def add_new_customers(self, customer): #create a customer
        """randomly creates new customers.        """

        self.customers.append(customer) #this function in my supermarket object literally creates other objects
    
    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        return None
    

            


# In[ ]:





# In[609]:


s = Supermarket()
s.add_new_customers(Customer('Narges'))


# In[610]:


s.add_new_customers(Customer('Felix'))


# In[611]:


#all customers start at entrance
s.customers


# In[622]:


#run this multiple times
s.next_minute()


# In[621]:


s.customers


# In[ ]:





# In[ ]:





# In[ ]:





# In[626]:


# Fake name generator
from faker import Faker
name = Faker().name()


# In[627]:


name


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




