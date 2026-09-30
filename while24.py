# Простая задача While24
n = int(input("Введите число N (> 1): "))
f1 = 1
f2 = 1
prinadlezhit = False
if n == 1:
    prinadlezhit = True
while f2 < n:
    sleduyushee = f1 + f2
    f1 = f2
    f2 = sleduyushee
    if f2 == n:
        prinadlezhit = True
if prinadlezhit == True:
    print("True (является числом Фибоначчи)")
else:
    print("False (НЕ является числом Фибоначчи)")