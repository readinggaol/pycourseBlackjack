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
    newHand = []
    newHand.append(r.choice(deck))
    newHand.append(r.choice(deck))
    return newHand


def getPlayerWager(pool):
    playerMoney = round(db.loadPlayerMoney(), 2)
    print("Money: " + str(playerMoney))

    while True:
        wagerAmount = int(input("Bet amount: "))
        if (playerMoney - wagerAmount) < 0:
            print("Insufficient funds. Please place a valid wager.")
            continue
        else:
            db.subtractPlayerMoney(wagerAmount)
            break


def dealAnotherCard(deck, hand):
    hand.append(r.choice(deck))
    return hand


def displayDealerShowCard(hand):
    print("\nDEALER'S SHOW CARD: ")
    print(hand[0][1] + " of " + hand[0][0].title())


def displayPlayerHand(hand):
    print("\nYOUR CARDS:")
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
    while handTotal > 21 and hasAce == True:
        for card in hand:
            if card[1] == "A" and card[2] == 11:
                card[2] == 1
                break
        handTotal = countHandValue(hand)





