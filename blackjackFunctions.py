import random as r
import db as db

def displayTitleInfo():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")


def createDeck():
    deck = []
    suits = ["hearts", "spades", "clubs", "diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    for suit in suits:
        counter = 0
        for rank in ranks:
            newCard = []
            newCard.append(suit)
            newCard.append(rank)
            newCard.append(values[counter])
            deck.append(newCard)
            counter += 1
    return deck


def dealHandOfCards(deck):
    #pop is used here instead of choice because the cards need to actually disappear from the deck when dealt
    newHand = []
    index = r.randint(0, len(deck) - 1)
    newCard = deck.pop(index)
    newHand.append(newCard)
    index = r.randint(0, len(deck) - 1)
    newCard = deck.pop(index)
    newHand.append(newCard)
    return newHand


def getPlayerWager():
    playerMoney = round(db.loadPlayerMoney(), 2)
    print("Money: " + str(playerMoney))

    while True:
        wagerAmount = int(input("Bet amount: "))
        if (playerMoney - wagerAmount) < 0:
            print("Insufficient funds. Please place a valid wager.")
            continue
        else:
            break
    return wagerAmount


def dealAnotherCard(deck, hand):
    index = r.randint(0, len(deck) - 1)
    newCard = deck.pop(index)
    hand.append(newCard)


def displayDealerShowCard(hand):
    print("\nDEALER'S SHOW CARD: ")
    print(hand[0][1] + " of " + hand[0][0].title())


def displayPlayerHand(hand):
    print("\nYOUR CARDS:")
    for card in hand:
        print(card[1] + " of " + card[0].title())


def displayDealerHand(hand):
    print("\nDEALER'S CARDS:")
    for card in hand:
        print(card[1] + " of " + card[0].title())


def decideHitOrStand(deck, hand):
    while True:
        userChoice = input("\nHit or stand? (hit/stand): ")
        if userChoice != "hit" and userChoice != "stand":
            print("Please enter a valid command.")
            continue
        else:
            break

    if userChoice == "hit":
        dealAnotherCard(deck, hand)
        return True
    elif userChoice == "stand":
        return False


def countHandValue(hand):
    handTotal = 0
    for card in hand:
        handTotal += card[2]
    return handTotal


#return true if there is at least one instance of an ace
#false will be returned if the loop completes without being true
def handHasAce(hand):
    for card in hand:
        if card[1] == "A":
            return True
    return False


def isBusted(hand):
    handTotal = countHandValue(hand)
    hasAce = handHasAce(hand)

    #if they have an ace and are above 21, start converting aces to 1 ONE AT A TIME
    #check to see if 21 is exceeded after converting each ace
    #after you change each ace value, change its rank to "a"
    #this will make it so that the handHasAce function will ACTUALLY only return true on "big" aces
    #it's maybe a little weird but simpler to read than some other alternatives
    while handTotal > 21 and hasAce == True:
        for card in hand:
            if card[1] == "A":
                card[2] == 1
                card[1] == "a"
                break
        hasAce = handHasAce(hand)
        handTotal = countHandValue(hand)

    if handTotal > 21:
        return True
    else:
        return False


def displayScoreDetermineWinner(playerHand, dealerHand, wager):
    playerScore = countHandValue(playerHand)
    dealerScore = countHandValue(dealerHand)

    #print scores
    if playerScore > 21:
        print("\nYOUR SCORE:\t" + "BUSTED")
    else:
        print("\nYOUR SCORE:\t" + str(playerScore))

    if dealerScore > 21:
        print("\nDEALER'S SCORE:\t" + "BUSTED")
    else:
        print("\nDEALER'S SCORE:\t" + str(dealerScore))

    #print result and handle money
    if isBusted(playerHand) and isBusted(dealerHand):
        print("Everyone busts.")
    elif not isBusted(playerHand) and isBusted(dealerHand):
        print("Player wins and dealer busts!")
        db.addPlayerMoney(wager)
    elif isBusted(playerHand) and not isBusted(dealerHand):
        print("Player busts and dealer wins!")
        db.subtractPlayerMoney(wager)
    #At this point I stop checking for busts because it's unnecessary
    elif playerScore == dealerScore:
        print("It's a tie!")
    elif playerScore > dealerScore:
        print("Player wins!")
        db.addPlayerMoney(wager)
    elif dealerScore > playerScore:
        print("Dealer wins!")
        db.subtractPlayerMoney(wager)
    else:
        print("I'm not sure what could cause this...uh oh.")





