import random

target = random.randint(1, 100)

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Введите ваше число: "))
    
    if guess < target:
        print("Загаданное число больше.")
    elif guess > target:
        print("Загаданное число меньше.")
    else:
        print("Поздравляю! Вы угадали число!")
        break
