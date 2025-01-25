class Mathematics:
    def __init__(self):
        print("Constructor executed.")
    def addition(self, number1, number2):
        return number1 + number2
    
    def subtraction(self, number1, number2):
        return number1 - number2
    
    def multiplication(self, number1, number2):
        return number1 * number2
    
    def division(self, number1, number2):
        return number1 / number2


mathematics = Mathematics()
print(mathematics.addition(10,20))
        