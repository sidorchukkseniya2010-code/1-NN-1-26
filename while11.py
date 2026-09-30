# Простая задача While11
n = int(input("Введите число N (>= 1): "))
k = 1
summa = 1
while summa < n:
    k = k + 1
    summa = summa + k
print("Наименьшее K:", k)
print("Итоговая сумма:", summa)