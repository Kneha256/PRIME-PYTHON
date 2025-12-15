#output for iterable in item if condition

square=[i*i for i in range(1,6) if i%2!=0]
print(square)

num=[-1,-2,-4,5,6,2,-9]
new=[0 if el<0 else el for el in num]
print(new)
