# Простая задача While2
a = float(input("Введите длину отрезка A: "))
b = float(input("Введите длину отрезка B (A > B): "))
ostatok = a
kolichestvo = 0
while ostatok >= b:
    ostatok = ostatok - b
    kolichestvo = kolichestvo + 1
print("Количество отрезков B внутри A:", kolichestvo)