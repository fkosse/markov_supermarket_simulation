import random 
import pandas as pd
import numpy as np

mx=pd.read_csv('mx.csv')
mx=mx.set_index('before')
mx

# What are the transition probabilities if the current state is fruit
mx['fruit'][0]

class Customer:
    """
    a single customer that moves through the supermarket in a MCMC simulation """
    
    def __init__(self, id, name):
        self.id=id
        self.name = name
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

class Supermarket:
    """manages multiple Customer instances that are currently in the market.    """
    
    def __init__(self):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.list = pd.DataFrame(columns=['timestamp', 'customer_name', 'customer_id', 'location'])
        
    def __repr__(self):
        return ''
    
    def get_time(self):
        hour = 7 + self.minutes // 60
        min = self.minutes % 60
        self.list.append(pd.Timestamp(year=2021, month=7, day=1, hour= hour, minute = min ))
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
   
s = Supermarket()
s.add_new_customers(Customer('Narges'))

s.add_new_customers(Customer('Felix'))

#all customers start at entrance
s.customers

#run this multiple times
s.next_minute()

s.customers

# Fake name generator
from faker import Faker
name = Faker().name()

name


'Hello'