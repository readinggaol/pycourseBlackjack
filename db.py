import csv

def loadPlayerMoney():
    #try to load the player's money and return the value
    #if the file does not exist, make one and return 0 to allow the game to still be played
    try:
        with open("money.txt", "r", newline="") as file:
            playerMoney = float(file.readline())
        return playerMoney
    except FileNotFoundError:
        print("Could not find the file named 'money.txt'.")
        print("Beginning game with starting money value of 0.")
        with open("money.txt", "w") as file:
            file.write(str(0))
        return 0
    except Exception as e:
        print("Unexpected error: ", type(e), e)
        print("Shutting down program.")
        exit()


def subtractPlayerMoney(wager):
    currentPlayerMoney = loadPlayerMoney()
    newPlayerMoney = currentPlayerMoney - wager
    with open("money.txt", "w") as file:
        file.write(str(newPlayerMoney))

def addPlayerMoney(wager):
    currentPlayerMoney = loadPlayerMoney()
    newPlayerMoney = currentPlayerMoney + wager
    with open("money.txt", "w") as file:
        file.write(str(newPlayerMoney))