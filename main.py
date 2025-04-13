import random 

class Deck():
    """
    Represents a standard 52-card deck used in the game.
    Handles creation, shuffling and dealing of cards.
    """
    def __init__(self):
        """Initialize a new deck with 52 cards (13 ranks in 4 suits)."""
        self.cards = []
        suits = ["spades" ,"clubs", "heart" , "diamonds"]
        ranks = [{'rank' : 'A' , "value" : 11 } ,
                {'rank' : '2' , "value" : 2 },
                {'rank' : '3' , "value" : 3 },
                {'rank' : '4' , "value" : 4 },
                {'rank' : '5' , "value" : 5 },
                {'rank' : '6' , "value" : 6 },
                {'rank' : '7' , "value" : 7 },
                {'rank' : '8' , "value" : 8 },
                {'rank' : '9' , "value" : 9 },
                {'rank' : '10' , "value" : 10 },
                {'rank' : 'J' , "value" : 10 },
                {'rank' : 'Q' , "value" : 10 },
                {'rank' : 'K' , "value" : 10 }]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """Randomize the order of cards in the deck if there are cards remaining."""
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, n):
        """
        Deal n cards from the deck.
        
        Args:
            n: Number of cards to deal
            
        Returns:
            List of dealt cards or message if deck is empty
        """
        cards_dealt = []      
        for i in range (n):
            if len(self.cards) == 0:
                return "deck empty"
            else:
                card = self.cards.pop() 
                cards_dealt.append(card)
        return cards_dealt
    
class Card():
    """Represents a single playing card with suit and rank."""
    def __init__(self, suit ,rank):
       self.suit = suit 
       self.rank = rank
    
    def __str__(self):
        """String representation of a card (e.g., 'A of spades')."""
        return f"{self.rank['rank']} of {self.suit}"

class Hand():
    """
    Represents a hand of cards held by either the player or dealer.
    Handles card management and score calculation.
    """
    def __init__(self, dealer = False):
        """
        Initialize a new hand.
        
        Args:
            dealer: Boolean indicating if this is the dealer's hand
        """
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_card(self, card_list):
        """Add one or more cards to the hand."""
        self.cards.extend(card_list)

    def calculate_value(self):
        """Calculate the total value of the hand."""
        self.value = 0
        has_ace = False
        
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == 'A':
                has_ace = True
        
        if has_ace and self.value > 21:
            self.value -= 10
    
    def get_value(self):
        """Get the current value of the hand."""
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        """Check if the hand is a blackjack (value equals 21)."""
        return self.get_value() == 21
    
    def display(self, show_all_dealer = False):
        """Display the cards in the hand."""
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        
        if not self.dealer:
            print("Value:", self.get_value())
        print()



class Game():
    def __init__(self):
        pass
    def play(self):
        game_number = 0
        games_to_play = 0
        
        while(games_to_play <= 0):
            try:
                games_to_play = int(input("How many games do you want to play?"))
            except:
                print("please enter number:")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand(dealer = True)

            for i in range (2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            print()
            print("*" * 30)
            print(f"Game:  {game_number} of {games_to_play}")
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose Hit or Stand : ").lower()
                print()
                while choice not in ["h","s","hit", "stand"]:
                    choice = input("Please enter Hit or Stand (H/S)").lower()
                    print()
                if choice in ["hit", 'h']:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue   
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value  = dealer_hand.get_value()
            
            dealer_hand.display(show_all_dealer = True)

            if self.check_winner(player_hand, dealer_hand):
                continue 
            print("Final Results")
            print("Your hand:",player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand ,dealer_hand , True)
        print("\n Thanks for playing")

    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:

            if player_hand.get_value() > 21:
                print("You busted. Dealer wins!")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win!")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack. a tie!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer have blackjack. Dealer wins!")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack., You win!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie!")
            else:
                print("Dealer Wins!")
            return True

        return False      



g = Game()
g.play()
