from guizero import App, Box, Text, PushButton
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.app = App("Rock, Paper, Scissors Game")
        self.game_box = Box(self.app, layout="grid", align="top")
        
        self.options = ["Rock", "Paper", "Scissors"]
        
        self.user_choice_text = Text(self.game_box, text="Select your choice:", grid=[0, 0, 2, 1])
        
        self.user_choice_buttons = []
        for i, option in enumerate(self.options):
            button = PushButton(self.game_box, text=option, command=lambda opt=option: self.play(opt), grid=[i, 1])
            self.user_choice_buttons.append(button)
        
        self.result_text = Text(self.game_box, text="", grid=[0, 2, 3, 1])
        
    def play(self, user_choice):
        computer_choice = random.choice(self.options)
        result = self.determine_winner(user_choice, computer_choice)
        self.result_text.value = f"You chose {user_choice}, computer chose {computer_choice}. {result}"
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif user_choice == "Rock":
            return "You win!" if computer_choice == "Scissors" else "Computer wins!"
        elif user_choice == "Paper":
            return "You win!" if computer_choice == "Rock" else "Computer wins!"
        elif user_choice == "Scissors":
            return "You win!" if computer_choice == "Paper" else "Computer wins!"
        else:
            return "Invalid choice"
        
game = RockPaperScissorsGame()
game.app.display()
