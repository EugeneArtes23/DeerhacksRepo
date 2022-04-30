import random
from time import sleep

total_balance = 100

class CF:
    def __init__(self, total_balance):
        self.total_balance = total_balance
        
    def play_game(self): 

        coin_faces = ['H', 'T']
        win_streak = 0
        run_state = True

        while run_state:
            
            print("Your total balance is $", self.total_balance)
            
            # Ask player for bet
            bet = 0
            while True:
                bet = input("How much would you like to bet?\n$")
                if bet.isnumeric():
                    bet = float(bet)
                else:
                    continue

                if bet > self.total_balance or bet < 0:
                    print("Bet should not be lower or higher than your total balance!")
                else:
                    self.total_balance = self.total_balance - bet
                    break

            # Ask player for Heads or Tails
            player_choice = ''
            while True:
                player_choice = input("Choose 'H' for Heads or 'T' for Tails:\n")
                if player_choice != 'H' and player_choice != 'T':
                    print("Not a valid choice!")
                else:
                    break

            # Win/Lose after choosing  
            flip_coin = random.choice(coin_faces)
            if player_choice == flip_coin:
                print("You win!")
                win_streak += 1
                print("You have a win streak of", win_streak)

                match win_streak:
                    case 1:
                        self.total_balance = 1*bet+self.total_balance+bet
                    case 2:
                        self.total_balance = 1.25*bet+self.total_balance+bet
                    case 3:
                        self.total_balance = 1.25*bet+self.total_balance+bet
                    case 4:
                        self.total_balance = 1.5*bet+self.total_balance+bet
                    case 5:
                        self.total_balance = 1.5*bet+self.total_balance+bet
                    case 6:
                        self.total_balance = 2*bet+self.total_balance+bet
                    case 7:
                        self.total_balance = 2*bet+self.total_balance+bet
                    case 8:
                        self.total_balance = 4*bet+self.total_balance+bet
                    case 9:
                        self.total_balance = 4*bet+self.total_balance+bet
                    case 10:
                        self.total_balance = 8*bet+self.total_balance+bet       
                    case _:
                        print("That's enough bro...")
                        break   
                
                print("You now have a balance of $", self.total_balance)            
                continue

            else:
                print("You lose!")
                print("You lost a win streak of", win_streak)                    
                print("You lost with $", self.total_balance)
                break

        return self.total_balance


game = CF(total_balance)
total_balance = game.play_game()
print("$", total_balance)