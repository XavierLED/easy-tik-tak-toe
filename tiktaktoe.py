map = [['.' for i in range(3)] for i in range(3)]


def main():
    player = ['x', 'o']
    i = 0
    printMap()
    
    while not win('x') and not win('o') and not isTie():
        i = i % 2
        square = None
        
        while True:
            square = input("player " + player[i] + " make your move (example: '1 2' for first row, second column):")
            square = square.split()
            square[0], square[1] = int(square[0]) - 1, int(square[1]) - 1
            
            if map[square[0]][square[1]] == '.':
                break

        place(square, player[i])
        i += 1
        
def printMap():
    for row in map:
        for column in row:
            print(column + '\t', end = '')
        print('\n')



def place(square, player):
    map[square[0]][square[1]] = player
    printMap()



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
    win = [player]*3
    window = ['.']*3

    for column in range(3):
        window[0] = map[0][column]
        window[1] = map[1][column]
        window[2] = map[2][column]
        if window == win:
            return True
    return False




def winInRow(player):
    win = [player] *3
    window = ['.']*3

    for row in range(3):
        window[0] = map[row][0]
        window[1] = map[row][1]
        window[2] = map[row][2]

        if window == win:
            return True
    
    return False


def winInDiagonals(player):
    win = [player]*3
    window = ['.']*3

    for i in range(3):
        window = map[i][i]
    if win == window:
        return True
    
    for i in range(3):
        window = map[i][2 - i]
    if win == window:
        return True
    
    return False




def isTie():
    for row in map:
        for column in row:
            if column == '.':
                return False
    return True

main()
