import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
             'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card:
    
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                created_card = Card(suit, rank)
                
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


class Player():
    
    def __init__(self, name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
        
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

    

player_1 = input("Enter name for Player 1: ")
player_2 = input("Enter name for Player 2: ")

player1 = Player(player_1)
player2 = Player(player_2)

game_deck = Deck()
game_deck.shuffle()
    
for x in range(26):
    player1.add_cards(game_deck.deal_one())
    player2.add_cards(game_deck.deal_one())
        
round_num = 0
game_on = True
while game_on:
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player1.all_cards) == 0:
        print(f"Game over! {player2.name} won the game")
        game_on = False
        break
    if len(player2.all_cards) == 0:
        print(f"Game over! {player1.name} won the game")
        game_on = False
        break
    
    player1_card = player1.remove_one()
    player2_card = player2.remove_one()
    
    
    if player1_card.value > player2_card.value:
        player1.add_cards(player1_card)
        player1.add_cards(player2_card)
    elif player1_card.value < player2_card.value:
        player2.add_cards(player2_card)
        player2.add_cards(player1_card)
    elif player1_card.value == player2_card.value:
        war_on = True
        player1_war = [player1_card]
        player2_war = [player2_card]
        while war_on:
            if len(player1.all_cards) < 3:
                print(f"{player1.name} can't declare war. {player2.name} has won the game")
                game_on = False
                break
            elif len(player2.all_cards) < 3:
                print(f"{player2.name} can't declare war. {player1.name} has won the game")
                game_on = False
                break
            print("War!")
            for num in range(3):
                player1_war.append(player1.remove_one())
                player2_war.append(player2.remove_one())
            if player1_war[-1].value > player2_war[-1].value:
                print(f"{player1.name} won the war")
                player1.add_cards(player1_war)
                player1.add_cards(player2_war)
                war_on = False
            elif player1_war[-1].value < player2_war[-1].value:
                print(f"{player2.name} won the war")
                player2.add_cards(player2_war)
                player2.add_cards(player1_war)
                war_on = False
            if len(player1.all_cards) == 0:
                war_on = False
            elif len(player2.all_cards) == 0:
                war_on = False
