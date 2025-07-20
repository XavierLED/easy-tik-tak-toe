import tkinter as tk
import tiktaktoe as ttt

map = [['.' for i in range(3)] for i in range(3)]
player = ['x','o']


root = tk.Tk()
root.title("Tik Tak Toe")

i = 0
#now its time to add the bot to play against
def onClick(row, column):
    global i 
    i = i % 2

    map[row][column] = player[i]
    i += 1

    if ttt.win('x', map) or ttt.win('o', map):
        label = tk.Label(text="A winner has been found!")
        label.grid(row=3, column = 0, columnspan=3, sticky="ew")


    elif ttt.isTie(map):
        label = tk.Label(text="There is a tie!")
        label.grid(row=3, column = 0, columnspan=3, sticky="ew")
    printMap()

def printMap():
    for i in range(3):
        for j in range(3):
            bnt = tk.Button(root, text=map[i][j], command= lambda i=i,j=j: onClick(i, j), width=20, height=10)
            bnt.grid(row=i, column=j, sticky="ns")

printMap()
root.mainloop()
