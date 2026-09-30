# Простая задача While23
a = int(input("Введите число A (> 0): "))
b = int(input("Введите число B (> 0): "))
while b > 0:
    ostatok = a % b
    a = b
    b = ostatok
print("Наибольший общий делитель (НОД):", a)