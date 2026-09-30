A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
s = 0
for i in range(A, B + 1):
    s += i ** 2
print(f"Сумма квадратов чисел от {A} до {B} равна: {s}")
