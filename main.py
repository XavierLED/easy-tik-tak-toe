import tkinter as tk
import tiktaktoe as ttt

map = [['.' for i in range(3)] for i in range(3)]


root = tk.Tk()
root.title("Tik Tak Toe")

def onClick():
    btn.config(text="clicked") #this shit doesnt work lol

def printMap():
    for i in range(3):
        for j in range(3):
            bnt = tk.Button(root, text=map[i][j], command=onClick)
            bnt.grid(row=i, column=j)

printMap()

root.mainloop()

#def main():
#    player = ['x', 'o']
#    i = 0
#    printMap()
#    
#    while not win('x') and not win('o') and not isTie():
#        i = i % 2
#        square = None
#        
#        while True:
#            square = input("player " + player[i] + " make your move (example: '1 2' for first row, second column):")
#            square = square.split()
#            square[0], square[1] = int(square[0]) - 1, int(square[1]) - 1
#            
#            if map[square[0]][square[1]] == '.':
#                break
#
#        place(square, player[i])
#        i += 1
#        
#def printMap():
#    for row in map:
#        for column in row:
#            print(column + '\t', end = '')
#        print('\n')
#
#def place(square, player):
#    map[square[0]][square[1]] = player
#    printMap()
#


