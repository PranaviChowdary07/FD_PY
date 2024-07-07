import tkinter

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
# create loop for window open
window.mainloop()
