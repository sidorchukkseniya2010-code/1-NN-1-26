# Простая задача While14
a = float(input("Введите число A (> 1): "))
k = 1
summa = 1.0
while summa + (1 / (k + 1)) < a:
    k = k + 1
    summa = summa + (1 / k)
print("Наибольшее K:", k)
print("Итоговая сумма:", summa)