import csv

def loadPlayerMoney():
    playerMoney = 0
    with open("money.txt", "r", newline="") as file:
        playerMoney = file.readline()
    return int(playerMoney)


def subtractPlayerMoney(wager):
    currentPlayerMoney = loadPlayerMoney()
    newPlayerMoney = currentPlayerMoney - wager
    with open("money.txt", "w") as file:
        file.write(str(newPlayerMoney))