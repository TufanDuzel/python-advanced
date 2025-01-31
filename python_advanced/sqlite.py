import sqlite3

def selectOperation():
    connection = sqlite3.connect("database\\chinook.db")
    
    # cursor = connection.execute("""select FirstName, LastName 
    #                            from customers 
    #                            where city = 'London'
    #                           order by FirstName""")
    
    # for row in cursor:
    #    print("First Name: " + row[0])
    #    print("Last Name: " + row[1])
    #    print("***********")
    
    
    cursor = connection.execute("""select city,count(*) 
                                from customers
                                group by city
                                having count(*)>1
                                order by count(*)
                                """)
                                
    for row in cursor:
        print("City: " + row[0])
        print("Total: " + str(row[1]))
        print("***********")
        
    connection.close()
    

def insertOperation():
    connection = sqlite3.connect("database\\chinook.db")
    
    connection.execute("""insert into customers 
                       (FirstName, LastName, City, Email)
                       values ('Tufan', 'Duzel', 'Skopje', 
                               'tufansahind@gmail.com')
                       """)
                       
    connection.commit()
    connection.close()


def updateOperation():
    connection = sqlite3.connect("database\\chinook.db")
    
    connection.execute("""update customers
                       set city = 'Istanbul'
                       where city = 'Skopje'
                       """)
                       
    connection.commit()
    connection.close()


def deleteOperation():
    connection = sqlite3.connect("database\\chinook.db")
    
    connection.execute("""delete from customers 
                       where CustomerId = 58
                       """)
                       
    connection.commit()
    connection.close()


# selectOperation()
# insertOperation()
# updateOperation()
# deleteOperation()