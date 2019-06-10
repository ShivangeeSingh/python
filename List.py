#!/bin/python3

a=[1,2,3,1,4,5,66,22,2,6,0,9]
c=[]
d=[]
print("1.For number > 5")
b=[i for i in a if i >5]
print(b)
c.append(b)

print("2.For number <= 2")
x=[i for i in a if i <= 2]
print(x)
d.append(x)

print("List 1 is: ",c)
print("List 2 is: ",d)
