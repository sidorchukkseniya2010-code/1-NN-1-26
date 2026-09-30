price = int(input("Введите цену 1 кг конфет: "))

for kg in range(1, 11):
    cost = kg * price
    print(f"Стоимость {kg} кг конфет: {cost:.2f}")
