import tkinter

board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

player_x = "X"
player_o = "O"
curr_player = player_x

color_x = "#5dade2"
color_o = "#f5b041"
color_background = "#e5e7e9"
color_winner = "#27ae60"
color_tie = "#dc7633"
color_loser = "#c0392b"

turns = 0
game_over = False


def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player

    if curr_player == player_o:
        board[row][column]["foreground"] = color_o
        curr_player = player_x
    else:
        board[row][column]["foreground"] = color_x
        curr_player = player_o
    
    label["text"] = curr_player+"'s turn"

    check_winner()

def check_winner():
    global turns, game_over

    turns += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] 
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_winner)
            for column in range(3):
                board[row][column].config(foreground=color_winner)
            game_over = True
            return
        
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] 
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_winner)
            for row in range(3):
                board[row][column].config(foreground=color_winner)
            game_over = True
            return
        
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_winner)
        for i in range(3):
            board[i][i].config(foreground=color_winner)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_winner)
        board[0][2].config(foreground=color_winner)
        board[1][1].config(foreground=color_winner)
        board[2][0].config(foreground=color_winner)
        game_over = True
        return
    
    if (turns == 9):
        game_over = True
        label.config(text="It's a tie!", foreground=color_tie)

        for row in range(3):
            for column in range(3):
                board[row][column].config(foreground=color_tie)


def new_game():
    global turns, game_over, curr_player

    turns = 0
    game_over = False
    curr_player = player_x

    label.config(text=curr_player+"'s turn", foreground="black")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_x)

window = tkinter.Tk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), 
                      background=color_background, foreground="black")
label.grid(row = 0, column = 0, columnspan=3, sticky="we", pady=0, padx=0)

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), foreground=color_x,
                                            width=3, height=2, borderwidth=0, pady=0, highlightthickness=0,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart Game", font=("Consolas", 20), foreground="black", 
                        command=lambda : new_game(), padx=0, pady=5, borderwidth=0, highlightthickness=0)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#center the game window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format window
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()