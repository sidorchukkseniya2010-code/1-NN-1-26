A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
total= 0
for i in range(A, B + 1):
    total += i
print(f"Сумма чисел от {A} до {B} равна: {total}")
