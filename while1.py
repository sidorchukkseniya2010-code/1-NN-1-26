# Простая задача While1
a = float(input("Введите длину отрезка A: "))
b = float(input("Введите длину отрезка B (A > B): "))
ostatok = a
while ostatok >= b:
    ostatok = ostatok - b
print("Длина незанятой части отрезка:", ostatok)