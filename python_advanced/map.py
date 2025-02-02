numbers = [1,2,3,4,5]

# squareOfNumbers = []
# for number in numbers:
#     squareOfNumbers.append(number*number)

squareOfNumbers = list(map(lambda number: number**2, numbers))

filteredNumbers = list(filter(lambda number: number>2, numbers))

from functools import reduce
multiplyOfNumbers = reduce(lambda x,y: x*y, numbers)

print(squareOfNumbers)
print(filteredNumbers)
print(multiplyOfNumbers)