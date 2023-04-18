from tkinter import *

class TicTacToe:
    def __init__(self):
        self.player = 1
        self.turns = 0
        self.game_over = False
        self.color1 = "blue"
        self.color2 = "red"
        self.create_board()

    def create_board(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.window = Tk()
        self.window.title("welcome to Tic tak toe Game")
        self.window.resizable(False, False)
        
        self.buttons = [[Button(self.window, text=' ', 
                                font=('Arial', 30), width=2, height=1, 
                                command=lambda row=i, col=j: 
                                self.play(row, col)) 
                         for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def play(self, row, col):
        if self.game_over:
            return
        if self.board[row][col] == ' ':
            if self.player == 1:
                self.buttons[row][col].config(text='2', fg=self.color1)
                self.board[row][col] = '2'
                self.player = 2
            else:
                self.buttons[row][col].config(text='1', fg=self.color2)
                self.board[row][col] = '1'
                self.player = 1
            self.turns += 1
            if self.check_win():
                self.game_over = True
                self.show_message("Player " + str(self.player) + " wins!")
            elif self.turns == 9:
                self.game_over = True
                self.show_message("It's a tie!")

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]!= ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i]!= ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]!= ' ':
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2]!= ' ':
            return True
        return False

    def show_message(self, message):
        popup = Toplevel()
        popup.title("Game Over")
        popup.geometry("200x100")
        label = Label(popup, text=message, font=('Arial', 18))
        label.pack(expand=True)
        button = Button(popup, text="OK", command=self.window.destroy, font=('Arial', 14))
        button.pack(pady=10)

    def start(self):
        self.window.mainloop()

if __name__ == '__main__':
    game = TicTacToe()
    game.start()
