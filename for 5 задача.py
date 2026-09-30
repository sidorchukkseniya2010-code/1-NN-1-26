price = float(input("Введите цену 1 кг конфет: "))
for i in range(1, 11):
    kg = i / 10.0
    cost = kg * price
    print(f"Стоимость {kg:.1f} кг конфет: {cost:.2f}")
