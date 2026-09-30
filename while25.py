# Простая задача While25
n = int(input("Введите число N (> 1): "))
f1 = 1
f2 = 1
while f2 <= n:
    sleduyushee = f1 + f2
    f1 = f2
    f2 = sleduyushee
print("Первое число Фибоначчи, большее N:", f2)