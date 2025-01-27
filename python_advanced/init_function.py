class Mathematics:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def addition(self):
        return self.number1 + self.number2
    
    def subtraction(self):
        return self.number1 - self.number2
    
    def multiplication(self):
        return self.number1 * self.number2
    
    def division(self):
        return self.number1 / self.number2


mathematics = Mathematics(10,20)
print(mathematics.addition())


class Person:
        def __init__(self, firstName, lastName):
            self.firstName = firstName
            self.lastName = lastName

person = Person("Tufan", "Duzel")
print(person.firstName)