#%%
name : str = "Tufan"
age : int = 30
isStudent : bool = True

#%%
def addNumbers(a: int, b : int) -> int:
    return a + b

addNumbers(4,5)

#%%
def processValue(value: int | str) -> str:
    if isinstance(value, int):
        return f"processed integer: {value}"
    else:
        return f"processed string: {value}"
    
processValue("Hey")
processValue([10, 20, 30])

#%%
from typing import List

def sumOfList(numbers: List[int]) -> int:
    return sum(numbers)

numbers = [1, 2, 3, 4]
total = sumOfList(numbers)