import csv
import random as r
import db as db

def displayTitleInfo():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")


def createDeck():
    deck = []
    suits = ["hearts", "spades", "clubs", "diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
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
    print("Please enter a number value.")




