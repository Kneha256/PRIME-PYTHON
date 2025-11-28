#calc count of i in given string
str = "Atrificial Intelligence"

new_str = str.lower()
count=0

for char in new_str:
    if (char == "i"):
        count+=1

print("count of i is", count)



