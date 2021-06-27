import blackjackFunctions as bf
import db as db

def main():
    deck = bf.createDeck()
    dealerHand = bf.dealHandOfCards(deck)
    playerHand = bf.dealHandOfCards(deck)
    willHit = True

    bf.displayTitleInfo()

    while True:
        wager = bf.getPlayerWager()
        bf.displayDealerShowCard(dealerHand)

        #handle all player actions here
        #modifying the player hand before coming to the end
        while willHit:
            bf.displayPlayerHand(playerHand)
            print(bf.countHandValue(playerHand))
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
        break




if __name__ == "__main__":
    main()