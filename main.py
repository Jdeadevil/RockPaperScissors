import random
import sys


class RockPaperScissors:
    def __init__(self):
        self.first_question = None
        self.play_again = None
        self.wins = 0
        self.losses = 0
        self.your_move = ""
        self.enemy_attack = ""
        self.enemy_moves = ["Rock", "Paper", "Scissors"]
        self.intro_text = "Hello, welcome to my Rock Paper Scissors game. Let's see how far you can get!"

    def run_game(self):
        self.first_question = input("Being round? (Y/N) ")
        self.first_question = self.first_question.upper()

        if self.first_question == "Y":

            self.crunch_answers()

            print(f"Computer chose {self.enemy_attack.title()}!")
            self.play_again = input("Would you like to play again? (Y/N) ")
            self.play_again = self.play_again.upper()

            if self.play_again == "Y":
                self.crunch_answers()
            elif self.play_again == "N":
                print("No problem, thanks for playing! Also please hire me.")
                sys.exit()

        elif self.first_question == "N":
            sys.exit()
        else:
            print("That isn't a valid response.")
            self.run_game()

    def make_enemy_move(self):
        self.enemy_attack = random.choice(self.enemy_moves)
        self.enemy_attack = self.enemy_attack.upper()
        return self.enemy_attack

    def crunch_answers(self):
        self.your_move = input("What do you want to pick? (Rock, Paper, Scissors) ")
        self.your_move = self.your_move.upper()
        self.enemy_attack = self.make_enemy_move()
        if self.your_move == "ROCK" and self.enemy_attack == "PAPER":
            self.losses += 1
        elif self.your_move == "ROCK" and self.enemy_attack == "SCISSORS":
            self.wins += 1
        elif self.your_move == "PAPER" and self.enemy_attack == "SCISSORS":
            self.losses += 1
        elif self.your_move == "PAPER" and self.enemy_attack == "ROCK":
            self.wins += 1
        elif self.your_move == "SCISSORS" and self.enemy_attack == "ROCK":
            self.losses += 1
        elif self.your_move == "SCISSORS" and self.enemy_attack == "PAPER":
            self.wins += 1
        elif self.your_move == self.enemy_attack:
            pass
        else:
            print("That isn't a valid move.")

        print(f"Computer chose {self.enemy_attack.title()}!")
        print(f"You: {self.wins}")
        print(f"Computer: {self.losses}")
        print("")
        self.play_again = input("Would you like to play again? (Y/N) ")
        self.play_again = self.play_again.upper()

        if self.play_again == "Y":
            self.crunch_answers()
        elif self.play_again == "N":
            print("No problem, thanks for playing! Also please hire me.")
            sys.exit()


if __name__ == "__main__":
    game = RockPaperScissors()
    game.run_game()

