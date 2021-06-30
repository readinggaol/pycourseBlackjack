import blackjackFunctions as bf
import db as db


def main():

    playAgain = True

    bf.displayTitleInfo()

    while playAgain:
        if(bf.isBankrupt()):
            bf.topUpBank()

        #the deck needs to be created inside the loop
        #otherwise, the pop() will slowly remove all cards from the deck
        deck = bf.createDeck()
        dealerHand = bf.dealHandOfCards(deck)
        playerHand = bf.dealHandOfCards(deck)

        wager = bf.getPlayerWager()
        bf.displayDealerShowCard(dealerHand)

        #handle all player actions here
        #modifying the player hand before coming to the end
        willHit = True
        while willHit:
            bf.displayPlayerHand(playerHand)
            willHit = bf.decideHitOrStand(deck, playerHand)
            if(bf.isBusted(playerHand)):
                print("You busted!")
                bf.displayPlayerHand(playerHand)
                break
            else:
                continue

        #handle all dealer actions here
        #modifying the dealer hand before coming to the end
        while not bf.isBusted(dealerHand) and bf.countHandValue(dealerHand) < 17:
            bf.dealAnotherCard(deck, dealerHand)

        bf.displayDealerHand(dealerHand)
        bf.displayScoreDetermineWinner(playerHand, dealerHand, wager)
        print("Money: " + str(db.loadPlayerMoney()))

        playAgain = bf.willPlayAgain()

    print("Bye!")




if __name__ == "__main__":
    main()