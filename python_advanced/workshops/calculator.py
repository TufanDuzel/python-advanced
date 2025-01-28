class Mathematics:
    def addition(self, number1, number2):
        return number1 + number2
    def subtraction(self, number1, number2):
        return number1 - number2
    def multiplication (self, number1, number2):
        return number1 * number2
    def division (self, number1, number2):
        return number1 / number2

mathematics = Mathematics()
    
while True:
    print("Please select the math operation you want to do.")
    operation = int(input("(1: Addition), (2: Subtraction), (3: Multiplication), (4: Division.): "))
    
    number1 = int(input("First Number: "))
    number2 = int(input("Second Number: "))
    
    if (operation == 1):
        print(mathematics.addition(number1, number2))
        break
    elif (operation == 2):
        print(mathematics.subtraction(number1, number2))
        break
    elif (operation == 3):
        print(mathematics.multiplication(number1, number2))
        break
    elif (operation == 4):
        print(mathematics.division(number1, number2))
        break
    else:
        print("Please select a transaction between: 1-4.")