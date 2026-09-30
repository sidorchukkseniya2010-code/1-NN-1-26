# Простая задача While12
n = int(input("Введите число N (> 1): "))
k = 1
summa = 1
while summa + (k + 1) <= n:
    k = k + 1
    summa = summa + k
print("Наибольшее K:", k)
print("Итоговая сумма:", summa)