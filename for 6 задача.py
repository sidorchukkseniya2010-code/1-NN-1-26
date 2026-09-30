price = float(input("Введите цену 1 кг конфет: "))
for i in range(6, 11):
    kg = i * 0.2
    cost = kg * price
    print(f"Стоимость {kg:.1f} кг конфет: {cost:.2f}")
