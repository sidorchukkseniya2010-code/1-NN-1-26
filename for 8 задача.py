A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
p = 1
for i in range(A, B + 1):
    p *= i
print(f"Произведение чисел от {A} до {B} равно: {p}")
