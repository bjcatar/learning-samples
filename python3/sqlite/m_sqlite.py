import sqlite3
import pprint

# https://realpython.com/data-engineer-interview-questions-python/

db = sqlite3.connect(':memory') # Using an in-memory database 
cur = db.cursor()

# Create tables
cur.execute(
  '''
  CREATE TABLE IF NOT EXISTS Customer (
    id integer PRIMARY KEY,
    firstname varchar(255),
    lastname varchar(255)
  )
  ''')
cur.execute(
  '''
  CREATE TABLE IF NOT EXISTS Item (
    id integer PRIMARY KEY,
    title varchar(255),
    price decimal
  )
  '''
)
cur.execute(
  '''
  CREATE TABLE IF NOT EXISTS BoughtItem (
    ordernumber integer PRIMARY KEY,
    customerid integer,
    itemid integer,
    price decimal,
    CONSTRAINT customerid FOREIGN KEY (customerid) REFERENCES Customer(id),
    CONSTRAINT itemid FOREIGN KEY (itemid) REFERENCES Item(id)
  )
  '''
)

# Populate tables
cur.execute(
  '''
  INSERT INTO Customer(firstname, lastname)
  VALUES ('Bob', 'Adams'),
         ('Amy', 'Smith'),
         ('Rob', 'Bennet');
  '''
)
cur.execute(
  '''
  INSERT INTO Item(title, price)
  VALUES ('USB', '10.2'),
         ('Mouse', '12.23'),
         ('Monitor', '199.99');
  '''
)
cur.execute(
  '''
  INSERT INTO BoughtItem(customerid, itemid, price)
  VALUES (1, 1, 10.2),
         (1, 2, 12.23),
         (1, 3, 199.99),
         (2, 3, 180.00),
         (3, 2, 11.23);
  '''
)

# SQL Aggregation functions
cur.execute(
  '''
  -- EXPLAIN QUERY PLAN -- commented out
  SELECT B.firstname, SUM(A.price)
  FROM BoughtItem A 
  INNER JOIN Customer B ON A.customerid = B.id
  GROUP BY B.firstname
  '''
)

pprint.pprint(cur.fetchall())