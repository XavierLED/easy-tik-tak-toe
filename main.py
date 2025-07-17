import tkinter as tk
import tiktaktoe as ttt

map = [['.' for i in range(3)] for i in range(3)]
player = ['x','o']


root = tk.Tk()
root.title("Tik Tak Toe")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

i = 0
def onClick(row, column):
    global i 
    i = i % 2

    map[row][column] = player[i]
    i += 1

    if ttt.win('x', map) or ttt.win('o', map):
        exit()

    elif ttt.isTie(map):
        exit()

    else:
        printMap()

def printMap():
    for i in range(3):
        for j in range(3):
            bnt = tk.Button(root, text=map[i][j], command= lambda i=i,j=j: onClick(i, j), width=20, height=10)
            bnt.grid(row=i, column=j, sticky="ns")

printMap()
if ttt.win('x', map) or ttt.win('o', map):
    exit()
elif ttt.isTie(map):
    exit()
root.mainloop()
