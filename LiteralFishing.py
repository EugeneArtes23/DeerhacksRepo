import enum
import random
from time import sleep

class CatchValues(enum.Enum):
    Tuna = 5
    Bass = 10
    Crate_of_Gold = 1000
    Crate_of_Fish = 500
    Swordfish = 250
    Shark = 750
    Whale = 1000
    Megalodon = 2000

class Literal_Fishing:
    def __init__(self,fish):
        self.fish = fish
    def play_game(self):
        
        # Possible catches the player can fish
        pool = ["Nothing","Boot","Seaweed","Tin Can","Goldfish","Tuna","Bass",
                "Crate of Randomness","Crate of Gold","Crate of Fish","Swordfish",
                "Shark","Whale","Megalodon"]

        # All print statements of player's catches
        if self.fish == "Yes":            
            player_fishing = random.choice(pool)
            if player_fishing == "Nothing":
                print("You got a Nothing!")                 

            elif player_fishing == "Boot":
                print("You got a Boot!")                 
                print("There's a snake in my boot!")                 

            elif player_fishing == "Seaweed":
                print("You got a Seaweed!")                 
                print("Seaweed = Manly Mustache")                 

            elif player_fishing == "Tin Can":
                print("You got a Tin Can!")                 
                print("Just a tin can.")                 

            elif player_fishing == "Goldfish":
                print("You got a Goldfish!")                 
                print("Top tier pet!")                 

            elif player_fishing == "Tuna":
                print("You got a Tuna!")                 
                print("Tuna tastes good... legit.")                 

            elif player_fishing == "Bass":
                print("You got a Bass!")                 
                print("Drop the BASS!")                 

            elif player_fishing == "Crate of Randomness":
                print("You got a Crate of Randomness!")                 
                print("I wonder what is inside?")
                print("You got a",random.choice(pool))                 

            elif player_fishing == "Crate of Gold":
                print("You got a Crate of Gold!")                 
                print("WOW! You struck GOLD!")                

            elif player_fishing == "Crate of Fish":
                print("You got a Crate of Fish!") 
                print("It's a lifetime supply of food!")     

            elif player_fishing == "Swordfish":
                print("You got a Swordfish!")                 
                print("Imagine fencing with those!") 

            elif player_fishing == "Shark":
                print("You got a Shark!")                 
                print("Jaws movies are realistic!")

            elif player_fishing == "Whale":
                print("You got a Whale!")                 
                print("I thought that was Moby Dick... It's just a regular whale.") 

            elif player_fishing == "Megalodon":
                print("You got a Megalodon!")                 
                print("Oh wow... I thought they were extinct!")                                                                                                                                                                     

        else:
            print("Call me again if you want to fish!")

print("Possible Catches:")
sleep(2)
print("Nothing")
print("Boot")
print("Seaweed")
print("Tin Can")
print("Goldfish")
print("Tuna")
print("Bass")
print("Crate of Randomness")
print("Crate of Gold")
print("Crate of Fish")
print("Swordfish")
print("Shark")
print("Whale")
print("Megalodon\n")
sleep(1.5)
player_fish = Literal_Fishing(input("Would you like to go fishing? (Yes/No): "))
print("*********J")
sleep(1)
print("*******J")
sleep(1)
print("*****J")
sleep(1)
print("***J")
sleep(1)
print("*J")
sleep(1)
player_fish.play_game()