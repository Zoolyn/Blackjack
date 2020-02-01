class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):

        # For ace
        if self.value == 1:
            return 'Ace of ' + str(self.suit)
        elif self.value == 11:
            return 'Jack of ' + str(self.suit)
        elif self.value == 12:
            return 'Queen of ' + str(self.suit)
        elif self.value == 13:
            return 'King of ' + str(self.suit)
        elif self.value == 'joker':
            return str(self.suit) + ' ' +  str(self.value)
        else:
            return str(self.value) + ' of ' + str(self.suit) 