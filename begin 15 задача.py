import math
S=int(input("Введите площадь S: "))
R = math.sqrt(S / math.pi)
L = 2 * math.pi * R
print("Радиус окружности: ", R)
print("Площадь круга: ", S)
print("Длина окружности: ", L)
