# Простая задача While27
n = int(input("Введите число N (оно является числом Фибоначчи): "))
f1 = 1
f2 = 1
nomer = 2
while f2 < n:
    sleduyushee = f1 + f2
    f1 = f2
    f2 = sleduyushee
    nomer = nomer + 1
print("Порядковый номер числа Фибоначчи N равен:", nomer)