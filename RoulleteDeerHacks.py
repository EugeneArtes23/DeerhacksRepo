import random

class Roullete:

    def __init__(self,bet):
        self.bet = bet

    def main(self):

        allNum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

        # red
        if self.bet == 1:
            spin = random.choice(allNum)
            print(spin)
            if spin%2 == 0:
                print("You Lost")
            else:
                print("You Won")

        #black
        elif self.bet == 2:
            spin = random.choice(allNum)
            print(spin)
            if spin% 2 == 0:
                print("You Won")
            else:
                print("You Lost")
        
        #green
        elif self.bet == 3:
            spin = random.choice(allNum)
            print(spin)
            if spin//2 == 0:
                print("You Won")
            else:
                print("You Lost") 

            
print ("Red/Odd = 1")
print ("Black/Even = 2") 
print ("Green/0 = 3")      
playerBet = Roullete(int(input('Place your bet, 1-3: ')))
playerBet.main()

    
    