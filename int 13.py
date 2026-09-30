n = int(input("Введите трехзначное число: "))
c = n // 100
ost = n % 100
res = ost * 10 + c
print("Полученное число:", res)
