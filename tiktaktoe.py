map = [["."]*3]*3
def main():
    player = ['x', 'o']
    i = 0
    while not win(x) and not win(o) and not isTie():
        i -= 1
        square = input("player " + player[i] + "make your move (example: 1,2 for first row, second column):")
        square = square.split()
        square[0], square[1] = int(square[0]), int(square[1])

        place(square, player[i])

def place(square, player):
    map[square[0], square[1]] = player

def win(player):
    if winInColumn(player):
        return True
    elif winInRow(player):
        return True
    elif winInDiagonals(player):
        return True
    else:
        return False
    
def winInColumn(player):

def winInRow(player):

def winInDiagonals(player):

def isTie():

