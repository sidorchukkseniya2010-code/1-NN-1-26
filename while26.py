# Простая задача While26
n = int(input("Введите число N (оно является числом Фибоначчи): "))
f1 = 1
f2 = 1
while f2 < n:
    sleduyushee = f1 + f2
    f1 = f2
    f2 = sleduyushee
print("Предыдущее число Фибоначчи:", f1)
print("Следующее число Фибоначчи:", f1 + f2)