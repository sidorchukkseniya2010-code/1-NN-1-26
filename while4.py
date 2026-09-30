# Простая задача While4
n = int(input("Введите число N (> 0): "))
proverka = 1
while proverka < n:
    proverka = proverka * 3
if proverka == n:
    print("True (число является степенью тройки)")
else:
    print("False (число НЕ является степенью тройки)")