# Простая задача While21
n = int(input("Введите число N (> 0): "))
est_nechet = False
while n > 0:
    cifra = n % 10
    if cifra % 2 != 0:
        est_nechet = True
    n = n // 10
if est_nechet == True:
    print("В числе ЕСТЬ нечетные цифры")
else:
    print("В числе НЕТ нечетных цифр")