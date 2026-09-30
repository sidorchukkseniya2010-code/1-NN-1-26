# Простая задача While18
n = int(input("Введите число N (> 0): "))
summa = 0
kolichestvo = 0
while n > 0:
    cifra = n % 10
    summa = summa + cifra
    kolichestvo = kolichestvo + 1
    n = n // 10
print("Количество цифр:", kolichestvo)
print("Сумма цифр:", summa)