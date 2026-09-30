# Простая задача While20
n = int(input("Введите число N (> 0): "))
est_dvoika = False
while n > 0:
    cifra = n % 10
    if cifra == 2:
        est_dvoika = True
    n = n // 10
if est_dvoika == True:
    print("В числе ЕСТЬ цифра 2")
else:
    print("В числе НЕТ цифры 2")