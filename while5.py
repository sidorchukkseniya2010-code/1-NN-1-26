# Простая задача While5
n = int(input("Введите число N (оно должно быть степенью двойки): "))
stepen = 0
tekushee = 1
while tekushee < n:
    tekushee = tekushee * 2
    stepen = stepen + 1
print("Показатель степени K равен:", stepen)