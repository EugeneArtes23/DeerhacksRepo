import random

class DiceGame:
    def __init__(self,roll = None):
        if roll is None:
            self.roll = None
        else:
            self.roll = roll

    def diceRoll(self):
        comRoll = random.randint(2,12)
        playerRoll = random.randint(2,12)

        if self.roll == "Yes":
            print("Enemy rolled", comRoll)
            print("You rolled", playerRoll)

            if playerRoll > comRoll:
                print("You Win!!")
            elif playerRoll == comRoll:
                print("Draw!")
            else:
                print("You Lose!")

        else:
            print ("Play Again Next Time!")
            
            
playerRoll = DiceGame(input("Would You Like to Roll the Dice? (Yes/No): "))
playerRoll.diceRoll()
        