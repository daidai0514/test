import random

card = ['3star', '2star', '1star']
rate = [2, 18, 80]

cards_list = random.choices(card, weights=(rate), k=100)
counts = [cards_list.count('3star'),cards_list.count('2star'),cards_list.count('1star')]

print(counts)