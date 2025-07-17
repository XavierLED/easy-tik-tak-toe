
def win(player, map):
    if winInColumn(player, map):
        return True
    elif winInRow(player, map):
        return True
    elif winInDiagonals(player, map):
        return True
    else:
        return False



def winInColumn(player, map):
    win = [player]*3
    window = ['.' for i in range(3)]

    for column in range(3):
        window[0] = map[0][column]
        window[1] = map[1][column]
        window[2] = map[2][column]
        if window == win:
            return True
    return False




def winInRow(player, map):
    win = [player] *3
    window = ['.']*3

    for row in range(3):
        window[0] = map[row][0]
        window[1] = map[row][1]
        window[2] = map[row][2]

        if window == win:
            return True
    
    return False


def winInDiagonals(player, map):
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




def isTie(map):
    for row in map:
        for column in row:
            if column == '.':
                return False
    return True
