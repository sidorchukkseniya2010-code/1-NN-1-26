# Простая задача While17
n = int(input("Введите число N (> 0): "))
print("Цифры числа справа налево:")
while n > 0:
    cifra = n % 10
    print(cifra)
    n = n // 10