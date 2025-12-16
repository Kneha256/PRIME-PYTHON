#question 1
with open("names.txt", "w") as f:
    total_name=int(input("Enter tatal number of names: "))
    for times in range(total_name):
        name=input("Enter names: ")
        f.write(name + "\n")

with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())
    d=f.readline()
    print(d)

#question 2
file=open("log.txt", "a")
file.write("\nProgram run successfully")

file=open("log.txt", "r")
print(file.read())

#question 3
l1=[12,45,25,87,2,9,10,40]
l2=[el for el in l1 if el>=25]
l2.sort()
print(l2)

#question4
import json
dic={
    "Delhi":"34M",
    "Mumbai":"21M",
    "Kolkata":"15M"
}

with open("cities.json", "w") as f:
    json.dump(dic, f, indent=4)

with open("cities.json", "r")as f:
    data=json.load(f)
    action=input("Enter get/update: ")
    if action=="get":
        print(data)
    else:
        new_city=input("Enter city name: ")
        city_pollution=input("Enter pollution: ")
        # data[new_city]=(city_pollution)
        data.update({new_city:city_pollution})
        for city, pollution in data.items():
            print(f"{city}:{pollution}")

with open("cities.json", "w") as f:
    new_data=json.dump(data, f, indent=4)

print("JSON file updated successfully")

# question 5
try:
    with open("data.txt", "r") as f:
        content=f.read()

except FileNotFoundError or FileExistsError:
    print("File not found....")

else:
    print("file found")

finally:
    print("Execution done successfully...")