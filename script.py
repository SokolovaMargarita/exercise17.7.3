per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int (input("Ввести сумму вклада:"))

deposit = [round(money*(percent/100)) for percent in per_cent.values()]
print("Накопленные средства за год:", deposit)
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max_deposit)