import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock Paper Scissors Game")

        self.player_score = 0
        self.computer_score = 0

        # Configure colors
        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50"
        self.button_hover_color = "#45a049"
        self.label_color = "#333333"

        # Background color
        self.window.configure(bg=self.bg_color)

        # Labels for displaying scores
        self.label_player_score = tk.Label(self.window, text="Your Score: 0", font=('Helvetica', 12), fg=self.label_color, bg=self.bg_color)
        self.label_player_score.pack(pady=(20, 5))

        self.label_computer_score = tk.Label(self.window, text="Computer Score: 0", font=('Helvetica', 12), fg=self.label_color, bg=self.bg_color)
        self.label_computer_score.pack()

        # Labels for displaying choices
        self.label_player_choice = tk.Label(self.window, text="Your Choice: ", font=('Helvetica', 12), fg=self.label_color, bg=self.bg_color)
        self.label_player_choice.pack(pady=(20, 5))

        self.label_computer_choice = tk.Label(self.window, text="Computer's Choice: ", font=('Helvetica', 12), fg=self.label_color, bg=self.bg_color)
        self.label_computer_choice.pack()

        # Create buttons for player choices
        self.button_rock = tk.Button(self.window, text="Rock", width=20, bg=self.button_color, fg="white", font=('Helvetica', 12, 'bold'), 
                                     activebackground=self.button_hover_color, command=lambda: self.play_game('Rock'))
        self.button_rock.pack(pady=10)

        self.button_paper = tk.Button(self.window, text="Paper", width=20, bg=self.button_color, fg="white", font=('Helvetica', 12, 'bold'), 
                                      activebackground=self.button_hover_color, command=lambda: self.play_game('Paper'))
        self.button_paper.pack(pady=10)

        self.button_scissors = tk.Button(self.window, text="Scissors", width=20, bg=self.button_color, fg="white", font=('Helvetica', 12, 'bold'), 
                                         activebackground=self.button_hover_color, command=lambda: self.play_game('Scissors'))
        self.button_scissors.pack(pady=10)

        # Reset button
        self.button_reset = tk.Button(self.window, text="Reset", width=20, bg="#f44336", fg="white", font=('Helvetica', 12, 'bold'),
                                      activebackground="#d32f2f", command=self.reset_game)
        self.button_reset.pack(pady=20)

    def play_game(self, player_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)

        # Display choices
        self.label_player_choice.config(text="Your Choice: " + player_choice)
        self.label_computer_choice.config(text="Computer's Choice: " + computer_choice)

        # Determine the winner
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
             (player_choice == 'Paper' and computer_choice == 'Rock') or \
             (player_choice == 'Scissors' and computer_choice == 'Paper'):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        # Update score labels
        self.label_player_score.config(text=f"Your Score: {self.player_score}")
        self.label_computer_score.config(text=f"Computer Score: {self.computer_score}")

        # Show result in messagebox
        messagebox.showinfo("Result", result)

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.label_player_score.config(text="Your Score: 0")
        self.label_computer_score.config(text="Computer Score: 0")
        self.label_player_choice.config(text="Your Choice: ")
        self.label_computer_choice.config(text="Computer's Choice: ")

# Create the main window
window = tk.Tk()
game = RockPaperScissorsGame(window)

# Run the main loop
window.mainloop()
