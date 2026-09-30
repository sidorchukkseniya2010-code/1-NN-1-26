# Простая задача While16
procent = float(input("Введите процент увеличения P (0 < P < 50): "))
distanciya = 10.0
summa_distanciy = 10.0
den = 1
while summa_distanciy <= 200.0:
    distanciya = distanciya + distanciya * (procent / 100.0)
    summa_distanciy = summa_distanciy + distanciya
    den = den + 1
print("Количество дней:", den)
print("Суммарный пробег лыжника:", summa_distanciy)