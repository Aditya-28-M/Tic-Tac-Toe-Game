import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x350")

# Track the current player (X starts)
current_player = "X"

# Create a list of buttons (3x3 grid)
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check for win or tie
def check_winner():
    # Check rows, columns and diagonals
    for i in range(3):
        # Rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        # Columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Check if board is full (tie)
def check_tie():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Button click handler
def on_click(r, c):
    global current_player

    # If button already clicked, ignore
    if buttons[r][c]["text"] != "":
        return

    # Set text to current player's symbol
    buttons[r][c]["text"] = current_player

    # Check for winner
    if check_winner():
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        root.destroy()
        return
    elif check_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        root.destroy()
        return

    # Switch player
    current_player = "O" if current_player == "X" else "X"
    turn_label.config(text=f"{current_player}'s Turn")

# UI - Label for player turn
turn_label = tk.Label(root, text="X's Turn", font=("Arial", 16))
turn_label.pack(pady=10)

# UI - Create 3x3 grid of buttons
frame = tk.Frame(root)
frame.pack()

for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

# Start the GUI event loop
root.mainloop()
