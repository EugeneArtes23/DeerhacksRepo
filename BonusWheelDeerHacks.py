import random

class BonusWheel:
    def __init__(self,spin):
        self.spin = spin
    def wheelSpin(self):
        spins = ["x2 Next Win","You Won Nothing","x3 Next Win","Bankrupt LMAO","Free Spin","Free Play"]

        if self.spin == "Yes":
            print(random.choice(spins))
        else:
            print("Come Back Next Time")

print ("Possible Outcomes:")
print ("x2 Next Win")
print ("You Won Nothing")
print ("x3 Next Win")
print ("Bankrupt LMAO")
print ("Free Spin")
print ("Free Play")

playerSpin = BonusWheel(input("Would You Like to Spin the Wheel? (Yes/No): "))
playerSpin.wheelSpin()