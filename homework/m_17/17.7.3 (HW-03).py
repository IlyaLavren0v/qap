per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

investment = int(input("Введите сумму вложений:"))
list_percent = list(per_cent.values())

deposit.append(int(investment / 100 * list_percent[0]))
deposit.append(int(investment / 100 * list_percent[1]))
deposit.append(int(investment / 100 * list_percent[2]))
deposit.append(int(investment / 100 * list_percent[3]))

print("Максимальный доход ваших вложений:", max(deposit))
