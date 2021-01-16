import random
suits = ['黑桃','紅心','方塊','梅花']
cardno = ['2','3','4','5','6','7','8','9','10','A','J','Q','K']

def make_cards():
    cards = []
    for s in suits:
        for i in cardno:
            cards.append(s+i)

    return cards
mycards = make_cards()
print(mycards)

givecard = random.choice(mycards)
print('===========')
print(givecard)