import math
a=int(input("Введите катет а: "))
b=int(input("Введите катет b: "))
c = math.sqrt(a**2 + b**2)
P = a + b + c
print("Гипотенуза: ", c)
print("Периметр: ", P)
