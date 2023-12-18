per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
investment = int(input("Введите сумму вложений:"))
list_percent = list(per_cent.values())
deposit = []

for i in list_percent:
    deposit.append(int(investment/100 * i))

print(max(deposit))