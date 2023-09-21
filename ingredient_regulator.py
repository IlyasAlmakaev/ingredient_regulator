# Рецепт для 48 булочек
# Нужно вычислить сколько нужно ингридиентов для одной булочки
# Формула какой-то ингридент разделённый на 48. Итак для каждого ингридиента
# Далее пользователь вводит кол-во булочек которых он хочет приготовить
# Высчитывается сколько нужно игридиентов для данного количества булочек
# Формула пропороция для одной булочки умножается на количетво необходимых булочек
# Показывается количество стаканов для каждого ингридиента для данного количества булочек

cup_of_sugar_48 = 1.5
cup_of_oil_48 = 1
cup_of_flour_48 = 2.75
buns = 48

cup_of_sugar = cup_of_sugar_48 / buns
cup_of_oil = cup_of_oil_48 / buns
cup_of_flour = cup_of_flour_48 / buns

print(cup_of_sugar, cup_of_oil, cup_of_flour)

current_buns = int(input('Сколько булочек вы хотите приготовить? '))
current_cup_of_sugar = cup_of_sugar * current_buns
current_cup_of_oil = cup_of_oil * current_buns
current_cup_of_flour = cup_of_flour * current_buns

print(f'Для {current_buns} булочек вам понадобиться:',
      f'{current_cup_of_sugar:.2f} стаканов сахара',
      f'{current_cup_of_oil:.2f} стаканов масла',
      f'{current_cup_of_flour:.2f} стаканов муки',
      sep='\n')