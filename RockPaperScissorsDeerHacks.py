import random
import enum

class Condition(enum.Enum):
    Win = 1
    Lose = 2
    Drew = 3

class Choices(enum.Enum):
    rock = 1 
    paper = 2
    scissors = 3

class RPS():
    def __init__(self):
        self.compChoice = Choices(random.randint(1,3)).name
        self.outcome = 'Win'

    def Play(self,action=str):
        if action == self.compChoice:
            self.outcome = Condition(3).name

        elif action == Choices(1).name:
            if self.compChoice == Choices(3).name:
                self.outcome = Condition(1).name
            else:
                self.outcome = Condition(2).name

        elif action == Choices(2).name:
            if self.compChoice == Choices(1).name:
                self.outcome = Condition(1).name
            else:
                self.outcome = Condition(2).name

        elif action == Choices(3).name:
            if self.compChoice == Choices(2).name:
                self.outcome = Condition(1).name
            else:
                self.outcome = Condition(2).name


