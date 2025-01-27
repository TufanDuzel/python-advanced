class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
person1 = Person("Tufan", "Duzel")
print(person1.firstName)

class Worker(Person):
    def __init__(self, salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
person2 = Worker(5000)
person3 = Customer("1111 1111 1111 1111")