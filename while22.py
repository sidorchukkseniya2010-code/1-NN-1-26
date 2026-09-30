# Простая задача While22
n = int(input("Введите простое число N (> 1): "))
delitel = 2
prostoe = True
while delitel * delitel <= n:
    if n % delitel == 0:
        prostoe = False
    delitel = delitel + 1
if prostoe == True:
    print("True (число простое)")
else:
    print("False (число составное)")