try:
    value = int(input("Please enter a character:"))
except ValueError:
    print("An error occurred: You did not enter a integer value!")
except:
    print("An error occurred.")
    
print("The program is over.")