from wallet import Client

client_1 = Client("Иван", "Петров", "Москва", "50 руб.")
print(client_1)

client_2 = Client("Егор", "Кранов", "Уссурийск", "")
client_3 = Client("Сергей", "Антоненко", "Бобруйск", "")

list_corporate = [client_1, client_2, client_3]

for guest in list_corporate:
    print(guest.getCorporate())