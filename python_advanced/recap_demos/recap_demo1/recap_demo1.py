customers = ["Chandler", "Ross", "Joe", "Monica", "Rachel", "Phoebe"]

fileToAppend = open("customers.txt", "a")

for customer in customers:
    fileToAppend.write(customer)
    fileToAppend.write("\n")
    
print("Customers added to the file successfully.")

fileToAppend.close()