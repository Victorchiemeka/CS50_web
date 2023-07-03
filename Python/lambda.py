people = [
    {"Name": "Harry", "House": "Amiri"},
    {"Name": "cho" ,"House": "Amiri"},
     {"Name": "Harry", "House": "Amiri"}
]

people.sort(key= lambda person: person["Name"])

print(people)