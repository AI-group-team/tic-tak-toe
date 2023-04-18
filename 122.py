from os import name
import tkinter as tk

class TicTacToe:
    def init(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.turn = "X"
        self.board = [[" " for _ in range(6)] for _ in range(6)]
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for row in range(6):
            button_row = []
            for col in range(6):
                button = tk.Button(self.master, text=" ", width=5, height=2,
                                   font=("Arial", 20, "bold"),
                                   command=lambda row=row, col=col: self.click_button(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def click_button(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn, fg=self.get_color(self.turn))
            if self.check_win(row, col):
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.switch_turn()

    def get_color(self, player):
        if player == "X":
            return "red"
        else:
            return "blue"

    def check_win(self, row, col):
        if (self.board[row][0] == self.board[row][1] == self.board[row][2] == self.board[row][3] == self.board[row][4] == self.board[row][5] == self.turn or 
            self.board[0][col] == self.board[1][col] == self.board[2][col] == self.board[3][col] == self.board[4][col] == self.board[5][col] == self.turn or 
            self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == self.board[4][4] == self.board[5][5] == self.turn or 
            self.board[0][5] == self.board[1][4] == self.board[2][3] == self.board[3][2] == self.board[4][1] == self.board[5][0] == self.turn):
            return True
        else:
            return False

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def show_winner(self):
        tk.messagebox.showinfo("Winner", f"Player {self.turn} wins!")
        self.reset_game()

    def show_draw(self):
        tk.messagebox.showinfo("Draw", "The game is a draw.")
        self.reset_game()

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def reset_game(self):
        self.turn = "X"
        self.board = [[" " for _ in range(6)] for _ in range(6)]
        for row in range(6):
            for col in range(6):
                self.buttons[row][col].config(text=" ", fg="black")

if name == "main":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()