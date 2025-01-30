import json

data = '{"firstName": "Tufan", "lastName": "Duzel"}'

y = json.loads(data)

print(y["firstName"])


customerDictionary = {
    "firstName": "Barney",
    "city": "London"
    }

customerJson = json.dumps(customerDictionary)
print(customerJson)