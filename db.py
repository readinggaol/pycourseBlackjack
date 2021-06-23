import csv

def loadPlayerMoney():
    playerMoney = 0
    with open("money", "r", newline="") as file:
        reader = csv.reader(file)
        playerMoney = next(reader)

    return int(playerMoney[0])


def subtractPlayerMoney(value):
        with open("money", "w") as file:
            writer = csv.writer(file)
            writer.writerow(value)
        return True