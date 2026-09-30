n = int(input("Введите N: "))
s = 0.0
k = 1.0
for i in range(1, n + 1):
    s += k * (1 + i / 10)
    k = -k
print("Результат:", s)
