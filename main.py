import tkinter as tk
import tiktaktoe as ttt
import robot as rb

map = [['.' for i in range(3)] for i in range(3)]
player = 'x'
robot = 'o'

root = tk.Tk()
root.title("Tik Tak Toe")

#now its time to add the bot to play against
def onClick(row, column):
    map[row][column] = player
    
    if ttt.win(player, map):
        label = tk.Label(text="Youre the Winner!")
        label.grid(row=3, column = 0, columnspan=3, sticky="ew")


    elif ttt.isTie(map):
        label = tk.Label(text="There is a tie!")
        label.grid(row=3, column = 0, columnspan=3, sticky="ew")

    moveRobot = rb.robotsMove(map)
    map[moveRobot[0]][moveRobot[1]] = robot

    if ttt.win(robot, map):
        label = tk.Label(text="Robot is the Winner")
        label.grid(row=3, column=0, columnspan=3, sticky="ew")

    printMap()

def printMap():
    for i in range(3):
        for j in range(3):
            bnt = tk.Button(root, text=map[i][j], command= lambda i=i,j=j: onClick(i, j), width=20, height=10)
            bnt.grid(row=i, column=j, sticky="ns")


printMap()
root.mainloop()

