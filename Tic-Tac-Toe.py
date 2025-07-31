import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.root.configure(bg="skyblue")

        self.current_player = tk.StringVar()
        self.current_player.set("Current Player : X")

        self.moves = 0
        self.player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, textvariable=self.current_player, font=('Times New Roman', 20),bg='skyblue',fg='blue')
        self.info_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(self.root, bg='blue', width=180, height=180, padx=3, pady=3)
                frame.grid_propagate(False)
                frame.grid(row=i + 1, column=j, padx=5, pady=5)
                button = tk.Button(self.root, text='', font=('normal', 40, 'normal'), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j), bg='white', fg='black', activebackground='red')
                button.grid(row=i + 1, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        if self.buttons[i][j]['text'] == '' and not self.check_winner():
            self.buttons[i][j]['text'] = self.player
            self.buttons[i][j]['fg'] = 'red' if self.player == 'X' else 'darkgreen'
            self.moves += 1
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"     Player {self.player} wins!          ")
                self.reset_board()
            elif self.moves == 9:
                messagebox.showinfo("Tic Tac Toe", "          It's a tie!          ")
                self.reset_board()
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.current_player.set(f"Current Player: {self.player}")

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True

        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['fg'] = 'black'
        self.player = 'X'
        self.moves = 0
        self.current_player.set(f"Current Player: {self.player}")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    icon = tk.PhotoImage(file="Tic-Tac-Toe-Game.png")
    root.iconphoto(False, icon)
    root.mainloop()
