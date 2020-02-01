import card
import random

class Deck:
    def __init__(self):
        self.cardlist = []
        self.numOfCards = 54
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    
    # Intial creation of the deck, this will also act as adding a full deck to another deck if needed
    # NOTE: make this will include jokers in the new deck so be sure to remove jokers before shuffling if needed, check removeJokers()
    def createDeck(self):        
        # Go through every suit
        for suit in self.suits:
            for value in range(1,14):
                new_card = card.Card(value, suit)
                self.cardlist.append(new_card)
        small_joker = card.Card('joker', 'small')
        large_joker = card.Card('joker', 'large')
        self.cardlist.append(small_joker)
        self.cardlist.append(large_joker)
        return
    
    # Shuffle the deck of cards
    def shuffleDeck(self):
        random.shuffle(self.cardlist)
        return

    # Draws the top card off the deck and returns that card object
    def drawCard(self):
        drawn_card = self.cardlist[0]
        del self.cardlist[0]
        return drawn_card

    # removes the joker from the deck if the cards are needed
    # NOTE: This should be done before the deck is shuffled as this method only removes the last two cards
    def removeJokers(self):
        del self.cardlist[-2:]
        return

    # Get the number of cards left in the deck
    def cardsLeft(self):
        return len(self.cardlist)

    # Helper Function used to check the contents of the deck
    def checkDeck(self):
        for card in self.cardlist:
            print(card)
        print(len(self.cardlist))
        return

