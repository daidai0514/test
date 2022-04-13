import random

arr = ['3star', '2star', '1star']
rate = [2, 18, 80]

def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

def random_card(number):
    card_list = [None]*number
    for i in range(number):
        card_list[i]=arr[random_index(rate)]
    
    return card_list

cards_list = random_card(1000)
counts = [cards_list.count('3star'),cards_list.count('2star'),cards_list.count('1star')]

print(counts)