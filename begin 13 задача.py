import math
R1=int(input("Введите радиус 1: "))
R2=int(input("Введите радиус 2: "))
S1 = math.pi * R1**2
S2 = math.pi * R2**2
S3 = S1 - S2
print("Площадь круга 1: ", S1)
print("Площадь круга 2: ", S2)
print("Площадь кольца: ", S3)
