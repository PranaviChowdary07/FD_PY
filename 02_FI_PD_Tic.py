import tkinter   # tk - interface(graphical) user interface library

def set_title(row,column):
    global curr_player 
    board[row][column]["text"] = curr_player   # mark the board

    if curr_player == playerO:   # switch player
        curr_player = playerX
    else:
        curr_player = playerO
    label["text"] = curr_player+"'s turn"
def new_game():
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
label.grid(row =0,column=0,columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text ="",font=("Consolas", 50,"bold"),background= color_gray,    foreground=color_blue,width=4,height=1,command=lambda row = row ,column= column:set_title(row,column))
        board[row][column].grid(row = row+1,column= column)
button = tkinter.Button(frame, text = "restart", font = ("Consolas",20),background=color_gray,foreground="white",   command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")

frame.pack()
# Center for window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
# create loop for window open
window.mainloop()
