import random
class Card(object):
    def __init__(self,suit,name,value):
        self.suit = suit
        self.name = name
        self.value = value
    def __add__(self, other_card):
        return self.value + other_card.value
    def __str__(self):
        return '{} of {} (value={})'.format(self.name,self.suit,self.value)
class Deck(object):
    def __init__(self):
        suits = ['Clubs','Hearts','Diamonds','Spades']
        name = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.cards = []
        for suit in suits:
            for index in range(len(name)):
                c = Card(suit,name[index],values[index])
                self.cards.append(c)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card
d = Deck()
d.shuffle()
player_hand = []
player_hand.append(d.deal())
player_hand.append(d.deal())
print(player_hand[0])
print(player_hand[1])
choice = input("Hit or Stand? ")
while choice != "Stand":
    user_hand = player_hand
    card_int_val = user_hand[0] + user_hand[:-1]
    print (card_int_val)
    if choice == "Hit":
        player_hand.append(d.deal())
        for card in player_hand:
            print(card)
        choice = input("Hit or Stand? ")
        
dealer_hand = []
dealer_hand.append(d.deal())
dealer_hand.append(d.deal())
for card in dealer_hand:
    print(card)
#while 
        
    
