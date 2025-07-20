import tiktaktoe as ttt

robot = 'o'
player = 'x'
def robotsMove(map):
    failure = [0, 0]
    
    for row in range(len(map)):
        for column in range(len(map[0])):
            
            if map[row][column] == '.':
                place(row, column, map)
                failure = [row, column]

            if ttt.win(robot, map):
                return row, column
           
            else:
                remove(row, column, map)
    
    return failure

def place(row, column, map):
    map[row][column] = 'o'

def remove(row, column, map):
    map[row][column] = '.'

