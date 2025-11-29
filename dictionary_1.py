#store data in key-value pair, unordered and keys are unique and immutable but values are mutable 
#empty dictionary
dict = {}

#dictionary with values

dict = {
    "name": "Neha",
    "age": 22,
    "marks": [35,67,89]
}

# print(dict, type(dict))
# print(len(dict))

# print(*dict["marks"])  #will return unpacked list

#methods in dictionary
print(dict.keys())   #will return all keys
print(dict.values())  #will return all values
print(dict.items())   #will return all key-value pairs as tuples in a list
print(dict.get("name"))  #will return value of key "name"
dict.update({"age":28})
print(dict)