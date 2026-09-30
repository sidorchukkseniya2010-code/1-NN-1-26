# Простая задача While15
procent = float(input("Введите процент увеличения P (0 < P < 25): "))
vklad = 1000.0
mesyac = 0
while vklad <= 1100.0:
    vklad = vklad + vklad * (procent / 100.0)
    mesyac = mesyac + 1
print("Количество месяцев:", mesyac)
print("Итоговый размер вклада:", vklad)