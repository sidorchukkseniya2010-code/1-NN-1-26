# Простая задача While3
n = int(input("Введите целое число N (> 0): "))
k = int(input("Введите целое число K (> 0): "))
chastnoe = 0
ostatok = n
while ostatok >= k:
    ostatok = ostatok - k
    chastnoe = chastnoe + 1
print("Частное от деления:", chastnoe)
print("Oстаток от деления:", ostatok)