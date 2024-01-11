tickets = int(input("Введите количество билетов: "))
total_cost = 0

for i in range(1, tickets + 1):
    age = int(input(f'Введите возраст посетителя {i}: '))
    ticket_cost = 0 if age < 18 else 990 if age < 25 else 1390
    total_cost += ticket_cost

total_cost *= 0.9 if tickets > 3 else 1

print(int(total_cost))
