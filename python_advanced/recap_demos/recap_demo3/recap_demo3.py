import sys

dataList = [7, "Tufan", 3, 0, "6"]

for data in dataList:
    try:
        print("Number: " + str(data))
        
        result = 1 / int(data)
        
        print("Result: " + str(result))
    except ValueError:
        print(str(data) + " is not a number.")
    except ZeroDivisionError:
        print(str(data) + " can not be divided.")
    except:
        print(str(data) + " could not be calculated!")
        print("Error: " + str(sys.exc_info()[0]))
    finally:
        print("The program is over.")