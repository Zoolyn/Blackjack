import pygame
import player
import deck
import card

# Initialize pygame
pygame.init()
pygame.font.init()

# Screen setup 
screen = pygame.display.set_mode((1080,720))

# Setup the Title and Icon
pygame.display.set_caption('Blackjack')
icon = pygame.image.load('images/poker.png')
pygame.display.set_icon(icon)

# Setting the fps
clock = pygame.time.Clock()

# Loading in the font
mainFont = pygame.font.SysFont('Times New Roman', 125)
subFont = pygame.font.SysFont('Times New Roman', 50)

# Import all the images for the deck
# Import all the photos and store them into a set that can neatly hold all the imported images
# There is no joker in this image set
importImgs = {}
suits = ['spades', 'hearts', 'diamonds', 'clubs']
for s in suits:
    for i in range(1,14):
        name = str(i) + '_' + s
        fullName = 'images/deck/' + name + '.png'
        importImgs[name] = pygame.image.load(fullName)
cardBack = pygame.image.load('images/deck/back.png')

# Helper functions
# refill the deck
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

# All functions needed to run the program
# display tester card in location
def test(x, player):
    #print(x)
    card = player.hand[x]
    cardFileName = str(card.value) + '_' + card.suit.lower()
    for i in range(x+1):
        screen.blit(importImgs[cardFileName], (15 * (i+1), 622))
# Display the deck in the upper right corner
def displayDeck():
    screen.blit(cardBack, (950, 100))
# Display horizontally centered text
def centeredText(text, size, color, height):
    font = pygame.font.SysFont('Times New Roman', size)
    textsurface = font.render(text, False, color)
    text_rect = textsurface.get_rect(center=(540, height))
    screen.blit(textsurface, text_rect)
# Display the cards in player's hand
def displayHand(player, position, revealed):
    # Check the position for the hand (0 == dealer and 1 == player)
    num = 1
    for card in player.hand:
        if revealed == True:
            if position == 0:
                cardFileName = str(card.value) + '_' + card.suit.lower()
                screen.blit(importImgs[cardFileName], (425 + 15 * (num), 100))
            else:
                cardFileName = str(card.value) + '_' + card.suit.lower()
                screen.blit(importImgs[cardFileName], (425 + 15 * (num), 520))
        else:
            if num == 1:
                cardFileName = str(card.value) + '_' + card.suit.lower()
                screen.blit(importImgs[cardFileName], (425 + 15 * (num), 100))
            else:
                screen.blit(cardBack, (425 + 15 * (num), 100))
        num+=1


# Title screen 
def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            # handling button presses for the title screen
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                if mouse[0] in range(340, 750) and mouse[1] in range(350,450):
                    intro = False
        screen.fill((0,153,0))
        # Create the title
        textsurface = mainFont.render('Blackjack', False, (255, 255, 255))
        text_rect = textsurface.get_rect(center=(540, 200))
        screen.blit(textsurface, text_rect)
        # Create the play button
        playsurface = subFont.render('Click Here to Play!', False, (255, 255, 255))

        text_rect1 = playsurface.get_rect(center=(540, 400))
        screen.blit(playsurface, text_rect1)
        pygame.display.update()
        clock.tick(60)

# Main game screen
def main_loop():
    main_loop = True
    # Create Deck object and prep it for the game
    main_deck = deck.Deck()
    main_deck.createDeck()
    main_deck.removeJokers()
    main_deck.shuffleDeck()
    # Deal cards to both players
    for i in range(0,4):
        if(i < 2):
            i = main_deck.drawCard()
            player1.addToHand(i)
        else:
            i = main_deck.drawCard()
            dealer.addToHand(i)
    while main_loop:
        for event in pygame.event.get():
            # handling button presses for the title screen
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] in range(400,465) and mouse[1] in range(330,370):
                    card = main_deck.drawCard()
                    # if we run out of cards
                    if main_deck.cardsLeft() == 0:
                        main_deck = refillDeck()
                        print('Refilling')
                    player1.addToHand(card)
                    if calculateHandValue(player1) > 21:
                        # deal cards to the dealer
                        while calculateHandValue(dealer) <= 17:
                            card = main_deck.drawCard()
                            # if we run out of cards
                            if main_deck.cardsLeft() == 0:
                                main_deck = refillDeck()
                                print('Refilling')
                            dealer.addToHand(card)
                        main_loop = False
                if mouse[0] in range(600, 710) and mouse[1] in range(330, 370):
                    while calculateHandValue(dealer) < 17:
                            card = main_deck.drawCard()
                            # if we run out of cards
                            if main_deck.cardsLeft() == 0:
                                main_deck = refillDeck()
                                print('Refilling')
                            dealer.addToHand(card)
                    main_loop = False
                print(mouse)
        # Basic Visual Outline creation
        screen.fill((0,153,0))
        centeredText('Dealer', 75, (255,255,255), 50)
        centeredText('Player', 75, (255,255,255), 670)
        textsurface = subFont.render('Hit', False, (255, 255, 255))
        screen.blit(textsurface,(400,325))
        textsurface1 = subFont.render('Stand', False, (255, 255, 255))
        screen.blit(textsurface1,(600,325))
        displayDeck()
        displayHand(player1,1,True)
        displayHand(dealer,0,False)
        pygame.display.update()
        clock.tick(60)

# Results screen of the round
def results_loop():
    print('this is the results page')
    results_loop = True
    while results_loop:
        for event in pygame.event.get():
            # handling button presses for the title screen
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                # If there is yes
                if mouse[0] in range(560, 630) and mouse[1] in range(380, 420):
                    return 1
                if mouse[0] in range(700, 760) and mouse[1] in range(380, 420):
                    pygame.quit()
                    exit()
        screen.fill((0,153,0))
        dealerScore = 'Dealer: ' + str(calculateHandValue(dealer))
        playerScore = 'Player: ' + str(calculateHandValue(player1))
        if calculateHandValue(dealer) > 21:
            if calculateHandValue(player1) < 21:
                centeredText('Player wins!', 75, (255,255,255), 250)
            else:
                centeredText('Dealer wins!', 75, (255,255,255), 250)
        else:
            if calculateHandValue(player1) > calculateHandValue(dealer) and calculateHandValue(player1) <= 21:
                centeredText('Player wins!', 75, (255,255,255), 250)
            else:
                centeredText('Dealer wins!', 75, (255,255,255), 250)
        centeredText(dealerScore, 75, (255,255,255), 50)
        centeredText(playerScore, 75, (255,255,255), 670)
        centeredText('Play again? Yes or No', 50, (255,255,255), 400)
        displayHand(player1,1,True)
        displayHand(dealer,0,True)
        pygame.display.update()
        clock.tick(60)
# Calls all the screens
# Create instances for players and deck
player1 = player.Player()
dealer = player.Player()
intro()
main_loop()
loop = results_loop()
while loop == 1:
    player1 = player.Player()
    dealer = player.Player()
    main_loop()
    loop = results_loop()