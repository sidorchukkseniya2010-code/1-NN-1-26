# Простая задача While10
n = int(input("Введите число N (> 1): "))
k = 0
proverka = 1
while proverka * 3 <= n:
    proverka = proverka * 3
    k = k + 1
print("Наибольшее число K, для которого 3 в степени K меньше или равно N:", k)