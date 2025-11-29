list=[1,2,3,4,8,6,5]
val=6

#linear search
index=0
for i in list:
    if val==i:
        print(index)
        break
    index+=1
     
#or using inbuilt function
if val in list:
    print(list.index(val))

