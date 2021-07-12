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


def isBankrupt():
    playerMoney = db.loadPlayerMoney()
    if playerMoney < 5:
        return True
    else:
        return False


def topUpBank():
    print("Your account's funds are lower than the minimum bet. Please deposit additional funds.")
    while True:
        try:
            newChips = int(input("Additional funds: "))
            if newChips < 5:
                print("You must enter a positive integer of at least 5.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print("Unexpected error. Shutting down program.", type(e), e)
            exit()

    db.addPlayerMoney(newChips)


def getPlayerWager():
    #get the player's current balance so we can make sure they have the money they want to bet
    try:
        playerMoney = round(db.loadPlayerMoney(), 2)
    except TypeError:
        print("File not loaded successfully. Exiting program.")
        exit()
    except Exception as e:
        print("Error fetching money value. Exiting program.", type(e), e)
        exit()

    print("\nMoney: " + str(float(playerMoney)))

    #**NOTE** no subtraction is actually done here, because the game could theoretically quit/crash before
    #the player actually wins or loses
    while True:
        try:
            wagerAmount = int(input("Bet amount: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        except Exception as e:
            print("Fatal error. Exiting program.", type(e), e)
            exit()

        if wagerAmount > 1000:
            print("Wager cannot exceed 1000.")
        elif wagerAmount < 5:
            print("Wager must be at least 5.")
        elif (playerMoney - wagerAmount) < 0:
            print("Insufficient funds. Please place a valid wager.")
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
        print(card[1].title() + " of " + card[0].title())


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
    # if they have an ace and are above 21, start converting aces to 1 ONE AT A TIME
    # check to see if 21 is exceeded after converting each ace
    # after you change each ace value, change its rank to "a"
    # this will make it so that the handHasAce function will ACTUALLY only return true on "big" aces
    # it's maybe a little weird but simpler to read than my other alternatives
    handTotal = countHandValue(hand)
    hasAce = handHasAce(hand)

    while handTotal > 21 and hasAce == True:
        for card in hand:
            if card[1] == "A":
                card[2] = 1
                card[1] = "a"
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

    #print scores -------------------------
    if playerScore > 21:
        print("\nYOUR POINTS:\t\t" + "BUSTED")
    else:
        print("\nYOUR POINTS:\t\t" + str(playerScore))

    if dealerScore > 21:
        print("\nDEALER'S POINTS:\t" + "BUSTED")
    else:
        print("\nDEALER'S POINTS:\t" + str(dealerScore))

    #print result and handle money -----------------
    if isBusted(playerHand) and isBusted(dealerHand):
        print("\nEveryone busts.")
    elif not isBusted(playerHand) and isBusted(dealerHand):
        print("\nPlayer wins and dealer busts!")
        db.addPlayerMoney(wager)
    elif isBusted(playerHand) and not isBusted(dealerHand):
        print("\nPlayer busts and dealer wins!")
        db.subtractPlayerMoney(wager)
    #At this point I stop checking for busts because it's unnecessary
    elif playerScore == dealerScore:
        print("\nIt's a tie!")
    elif playerScore > dealerScore or (playerScore < dealerScore and isBusted(dealerHand)):
        if playerScore == 21:
            print("\nBLACKJACK! 3:2 Payout of: " + str(wager * 1.5))
            db.addPlayerMoney(round((wager * 1.5), 2))
        else:
            print("\nPlayer wins!")
            db.addPlayerMoney(wager)
    elif dealerScore > playerScore:
        print("\nDealer wins!")
        db.subtractPlayerMoney(wager)
    else:
        print("Unknown error.")


def willPlayAgain():
    while True:
        userChoice = input("Play again? (y/n): ")
        if userChoice.lower() != "y" and userChoice.lower() != "n":
            print("Please enter a valid command.")
            continue
        else:
            if userChoice == "y":
                return True
            else:
                return False






