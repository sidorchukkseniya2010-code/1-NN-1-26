# Простая задача While13
a = float(input("Введите число A (> 1): "))
k = 1
summa = 1.0
while summa <= a:
    k = k + 1
    summa = summa + (1 / k)
print("Наименьшее K:", k)
print("Итоговая сумма:", summa)