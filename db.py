import csv

def loadPlayerMoney():
    try:
        with open("money.txt", "r", newline="") as file:
            playerMoney = float(file.readline())
        return int(playerMoney)
    except FileNotFoundError:
        print("Could not find the file named 'money.txt'.")
    except Exception:
        print("Must be the wrong error?")


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