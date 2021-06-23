import blackjackFunctions as bf
import db as db

def main():
    deck = bf.createDeck()
    pool = 0
    dealerHand = bf.dealHandOfCards(deck)
    playerHand = bf.dealHandOfCards(deck)
    willHit = True

    bf.displayTitleInfo()

    while True:
        # bf.getPlayerWager(pool)
        bf.displayDealerShowCard(dealerHand)
        while willHit:
            bf.displayPlayerHand(playerHand)
            print(bf.countHandValue(playerHand))
            willHit = bf.decideHitOrStand(deck, playerHand)





if __name__ == "__main__":
    main()