import random
class RPS:
    def __init__(self,action):
        self.action = action
        
    def gameRPS(self) -> str:
        reaction = ["Rock","Paper","Scissors"]
        ranReaction = random.choice(reaction)
        if self.action == ranReaction:

            print("Enemy plays",ranReaction,", it's a draw")
            
        elif self.action == "Rock":

            if ranReaction == "Scissors":
                print("Enemy plays",ranReaction,", you win!")
                
            else:
                print("Enemy plays",ranReaction,", you lose!")
                
        elif self.action == "Paper":

            if ranReaction == "Rock":
                print("Enemy plays",ranReaction,", you win!")
                
            else:
                print("Enemy plays",ranReaction,", you lose!")
               
        elif self.action == "Scissors":

            if ranReaction == "Paper":
                print("Enemy plays",ranReaction,", you win!")
               
            else:
                print("Enemy plays",ranReaction,", you lose!")
        else:
            print("Wrong Move")     
playerAction = RPS(input("Enter Choice (Rock/Paper/Scissors): "))
playerAction.gameRPS()