from math import sqrt
a=int(input("what is a: "))
b=int(input("what is b: "))
c=int(input("what is C: "))
s=(a+b+c)/2
Area=sqrt(s*(s-a)*(s-b)*(s-c))
print(Area)
