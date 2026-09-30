# Простая задача While19
n = int(input("Введите число N (> 0): "))
perevernutoe = 0
while n > 0:
    cifra = n % 10
    perevernutoe = perevernutoe * 10 + cifra
    n = n // 10
print("Перевернутое число N:", perevernutoe)