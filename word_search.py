#creat, add, and read using with
# with open("sample2.txt", "x") as f:
#     f.write("this is a demo file \nto store some words\nfor the Python activity \nThat is to be solved by us.")
# with open("sample2.txt", "r") as f:
#     print(f.read())

data= True
line=1
word="python"

with open("sample2.txt", "r") as f:
    while data:
        data=f.readline()

        if word in data:
            print(f"{word} found at {line}")
            break
        
        print(data)
        line+=1
            
