

from asyncore import read

import json

with open("json/person.json") as file:
    data=json.load(file)


print(data)
print(type(data))
print(data["firstName"])