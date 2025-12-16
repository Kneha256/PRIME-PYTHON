# java script object notation - A data format, not a programming structure
# stores values in key value pairs
# similar to python dictionary
# data exchange between client and server
# for dealing with json data we import module json
#json module help to convert json to python or python to json
# python and json
# list = array
# Non = null
# dictionary = object
# str = string

#load while json to python
import json
json_str='{"name":"shubhankar", "isTeacher":true}'
py_obj=json.loads(json_str)
print(type(py_obj), py_obj)

#dumps/dump - while python to json
py_obj={
    "name":"neha",
    "age":22,
    "isStudent":True
}

json_str=json.dumps(py_obj)
print(type(json_str), json_str)

#load/dump for dealing with json files
with open("data.json", "r") as f:
    py_obj=json.load(f)
    print(type(py_obj), py_obj)