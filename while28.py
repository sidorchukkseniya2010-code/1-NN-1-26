# Простая задача While28
eps = float(input("Введите точность epsilon (> 0): "))
a1 = 0.0
a2 = 2.0
k = 2
while abs(a2 - a1) >= eps:
    a1 = a2
    a2 = 2.0 + 1.0 / a1
    k = k + 1
print("Номер K:", k)
print("Элемент A K-1:", a1)
print("Элемент A K:", a2)