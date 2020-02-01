import deck
import card
import player

def main():
    print('Now playing blackjack!')
    # There is only one player in blackjack, not including the dealer
    player1 = player.Player()
    dealer = player.Player()
    main_deck = deck.Deck()
    main_deck.createDeck()
    main_deck.removeJokers()
    main_deck.shuffleDeck()
    # Main game loop
    while(True):
        playerChoice = None
        print('Dealing your cards')
        # deal two cards to the player and the dealer
        for i in range(0,4):
            if(i < 2):
                i = main_deck.drawCard()
                player1.addToHand(i)
            else:
                i = main_deck.drawCard()
                dealer.addToHand(i)
        # First display of both hands
        displayHand(dealer, True)
        displayHand(player1, False)
        # Player Action
        playerHandValue = calculateHandValue(player1)
        while(playerHandValue < 21):
            playerChoice = input('Would you like to hit or stand? ')
            # Input Check
            playerChoice = checkInput('hs', playerChoice)
            # Player is done
            if(playerChoice == 'stand' or playerChoice == 's'):
                break
            else:
                # Draw a card to deal to give the player
                # check if main_deck still has cards
                if(main_deck.cardsLeft() == 0):
                    main_deck = refillDeck()
                hit_card = main_deck.drawCard()
                player1.addToHand(hit_card)
                # Update the playerHandValue
                playerHandValue = calculateHandValue(player1)
                displayHand(player1, False)
        print('End of player\'s turn')
        displayHand(player1, False)
        print(playerHandValue)
        if(playerHandValue > 21):
            print('You Busted! Better luck next time!')
        else:
            # Deal with player vs dealer match
            # Add card to dealers hand until it is greater than or equal to 17
            dealerhand = calculateHandValue(dealer)
            while(dealerhand <= 17):
                if(main_deck.cardsLeft() == 0):
                    main_deck = refillDeck()
                drawnCard = main_deck.drawCard()
                dealer.addToHand(drawnCard)
                dealerhand = calculateHandValue(dealer)
            # Check if player has a higher score than the dealer
            playerhand = calculateHandValue(player1)
            displayHand(dealer, False)
            displayHand(player1, False)
            # Check if the dealer has busted or not
            if dealerhand > 21:
                # If both the player and dealer bust then the player loses
                if playerHandValue > 21:
                    print('Both you and dealer Busted! You lose!')
                print('Dealer Busted! You Win! :D')
            # If the dealer doesn't bust we have to compare hands
            else:
                if dealerhand >= playerHandValue:
                    print('Dealer wins!')
                else:
                    print('Player wins!')
            print(f'Player: {playerHandValue}')
            print(f'Dealer: {dealerhand}')
        playAgain = input('Would you like to play again (yes or no)? ')
        playAgain = checkInput('yn', playAgain)
        # Set up the new game
        if playAgain == 'yes' or playAgain == 'y':
            player1 = player.Player()
            dealer = player.Player()
        else:
            break

# refill the deck when needed
def refillDeck():
    # Create a new deck 
    main_deck = deck.Deck()
    main_deck.createDeck()
    main_deck.removeJokers()
    main_deck.shuffleDeck()
    return main_deck

# Calculate the value of the cards in the players hand
def calculateHandValue(curr_player):
    
    total_value = 0
    # Go through the curr_player hand and add up the values

    # If there is an Ace in the hand we wait to see the best fit for the Ace
    if any(x.value == 1 for x in curr_player.hand):
        card_values = []
        numAces = 0
        for card in curr_player.hand:
            card_values.append(card.value)
        for value in card_values:
            # Add all the non-Ace cards
            if value != 1:
                if value > 10:
                    total_value += 10
                else:
                    total_value += value
            else:
                numAces += 1
        # Check total_value
        for i in range(numAces):
            # If we need the Ace to be 11
            if total_value <=10:
                total_value += 11
            # If we need the Ace to be 1
            else:
                total_value += 1                                                                                                                  
    # If there is not an Ace in the hand just add up the values
    else:
        for card in curr_player.hand:
            # This is for face card
            if card.value > 10:
                total_value += 10
            else:
                total_value += card.value
    return total_value

# This will print out a display of the player's hand in the console
# Input: curr_player is the current player object, and isDealer is boolean to see if player is dealer or not
def displayHand(curr_player, isDealer):
    # Display for dealer's first hand
    if isDealer == True:
        print('Dealer:')
        print('[' + str(curr_player.hand[0]) + ']\t[\t]')
    # Display for rest of cases
    else:
        print('Player:')
        for card in curr_player.hand:
            print('[' + str(card) + ']', end='\t')
        print()

# Input check tool
'''
types:
-hs
-yn
'''
def checkInput(type, answer):
    # hit or stand input check
    correct_answer = None
    if type == 'hs':
        if any([answer == 'hit', answer == 'stand', answer == 'h', answer == 's']):
            correct_answer = answer
        else:
            while(True):
                print('Error in input!')
                print('Please choose one of the following: ')
                print('- hit or h')
                print('- stand or s')
                correct_answer = input('Would you like to hit or stand? ')
                if any([correct_answer == 'hit', correct_answer == 'stand', correct_answer == 'h', correct_answer == 's']):
                    break
    # yes or no input check
    elif type == 'yn':
        if any([answer == 'yes', answer == 'no', answer == 'y', answer == 'n']):
            correct_answer = answer
        else:
            while(True):
                print('Error in input!')
                print('Please choose one of the following: ')
                print('- yes or y')
                print('- no or n')
                correct_answer = input('Would you like to play again? ')
                if any([correct_answer == 'yes', correct_answer == 'no', correct_answer == 'y', correct_answer == 'n']):
                    break
    return correct_answer

if __name__ == '__main__':
    main()