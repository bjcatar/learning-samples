from sqlalchemy import MetaData, Table, Column, String, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db 

# https://itnext.io/sqlalchemy-orm-connecting-to-postgresql-from-scratch-create-fetch-update-and-delete-a86bc81333dc

class Database():
  # replace the user, password, hostname and database according to your configuration according to your information
  engine = db.create_engine('postgresql://localhost/test')
  
  def __init__(self):
    self.connection = self.engine.connect()
    print("DB Instance created")
  
  def saveData(self, customer):
    #   self.connection.execute(f"""INSERT INTO customer(name, age, email, address, zip_code) 
    #   VALUES('{customer.name}', '{customer.age}', '{customer.email}', '{customer.address}', '{customer.zip_code}')""")  
    session = Session(bind=self.connection)        
    session.add(customer)
    session.commit()
  
  def fetchUserByName(self):
    meta = MetaData()
    customer = Table('customer', meta, 
                    Column('name'),
                    Column('age'),
                    Column('email'),
                    Column('address'),
                    Column('zip_code'))
    data = self.connection.execute(customer.select())
    for cust in data:
        print(cust)
  
  def fetchAllUsers(self):
    # bind an individual Session to the connection
    self.session = Session(bind=self.connection)        
    customers = self.session.query(Customer).all()
    for cust in customers:
        print(cust)
  
  def fetchByQyery(self, query):
    fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
    
    for data in fetchQuery.fetchall():
        print(data)
  
  def updateCustomer(self, customerName, address):
    session = Session(bind=self.connection)   
    dataToUpdate = {Customer.address: address}    
    customerData = session.query(Customer).filter(Customer.name==customerName)
    customerData.update(dataToUpdate)
    session.commit()

  def deleteCustomer(self, customer):
    session = Session(bind=self.connection)       
    customerData = session.query(Customer).filter(Customer.name==customer).first()
    session.delete(customerData)
    session.commit()
            
Base = declarative_base()

class Customer(Base):
  """Model for customer account."""
  __tablename__ = 'customer'
  name = Column(String)
  age = Column(Integer)
  email = Column(String)
  address = Column(String)
  zip_code = Column(String)
  id = Column(Integer, primary_key=True)
  
  def __repr__(self): 
    return "<Customer(name='%s', age='%s', email='%s', address='%s', zip code='%s')>" % (self.name, self.age, self.email, self.address, self.zip_code)