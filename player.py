class Player:
    def __init__(self):
        self.player = 0
        self.hand = []
        self.value = 0
    
    def addToHand(self, card):
        self.hand.append(card)
        return

    # Check the hand of player
    def checkHand(self):
        for card in self.hand:
            print(card)
        return