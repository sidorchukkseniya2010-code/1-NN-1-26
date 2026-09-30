# Простая задача While6
n = int(input("Введите число N (> 0): "))
dvoinoy_factorial = 1
while n > 0:
    dvoinoy_factorial = dvoinoy_factorial * n
    n = n - 2
print("Двойной факториал равен:", dvoinoy_factorial)