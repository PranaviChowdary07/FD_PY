import tkinter   # tk - interface(graphical) user interface library

def set_title(row,column):
    pass
#Players
playerX = "X"
playerO = "O"
curr_player = playerX

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

# Window 
window = tkinter.Tk()  # Create game wimdow
window.title("Tic Tac Toe")
window.resizable(False, False)

# components for game
frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=  curr_player+"'S turn",font  = ("Consolas", 20),background= color_gray,foreground="white")
label.grid(row =0,column=0,columnspan=3)

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text ="",font=("Consolas", 50,"bold"),background= color_gray,foreground=color_blue,width=4,height=1,command=lambda row = row ,column= column:set_title(row,column))
        board[row][column].grid(row = row+1,column= column)
frame.pack()
# create loop for window open
window.mainloop()
