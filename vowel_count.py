str = "Artificial intelligence"

new_str = str.replace(" ","").lower()
vowels= "aeiou"
count=0

for char in new_str:
    if char in vowels:
        count+=1
        print(f"{char}", end=",")

print("\ntotal number of vowels are:")
print(count)