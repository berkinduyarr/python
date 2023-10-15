# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 23:07:26 2023

@author: Berkin
"""

import sqlite3


def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    
    
    #cursor = connection.execute("select FirstName,LastName from customers where city='Prague' or city='Berlin' order by FirstName,LastName desc")
    
    
    #for row in cursor:
    #     print("First Name = "+row[0])
    #     print("Last Name = "+row[1])
    #     print("********")
    
    # cursor = connection.execute("""select city,count (*) from Customers
    #                             group by city having count(*)>1 
    #                             order by count(*) desc""")
    # for row in cursor:
    #     print("City= "+row[0])
    #     print("Count = "+str(row[1]))
    #     print("********")
    
    
    cursor = connection.execute("select FirstName,LastName from customers where FirstName like '%a%'")
    
    
    for row in cursor:
        print("First Name = "+row[0])
        print("Last Name = "+row[1])
        print("********")
        
    connection.close()
    
selectOperasyonlari()

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("insert into customers (firstName,LastName,city,email)values('Begüm','Duyar','Ordu','begumduyar@gmail.com')")
    
    connection.commit()
    connection.close()       

# insertCustomer()

def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("update customers set city='Berlin' where city='Prague'")
    
    connection.commit()
    connection.close()
    
# updateCustomer()

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("Delete from customers where city='London' or country='Brazil'")
    
    connection.commit()
    connection.close()

# deleteCustomer()

       
def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("select albums.Title, artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId")
    
    
    for row in cursor:
        print("Title = "+row[0]+"Name = "+row[1])
        
    connection.close()
 
joinOperasyonlari()
        


             
     
