# Простая задача While9
n = int(input("Введите число N (> 1): "))
k = 1
proverka = 3
while proverka <= n:
    proverka = proverka * 3
    k = k + 1
print("Наименьшее число K, для которого 3 в степени K больше N:", k)