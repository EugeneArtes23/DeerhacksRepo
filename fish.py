import random

fishvalue = random.randint(1,10)

match fishvalue:
    case 1:
        prize = -20
        message = "You caught a Leather Boot!"
    case 2:
        prize = -10
        message = "You caught a crab!"
    case 3:
        prize = 5
        message = "You caught a Trout! There's no doubt!"
    case 4:
        prize = 8
        message = "You caught a dace! Hope you have some space!"
    case 5:
        prize = 10
        message = "You caught a Sea Bass! Wait, it's at least a  c+!"
    case 6:
        prize = 15
        message = "You caught a koi! I don't know why it's so shy.. or such a bad speller..."
    case 7:
        prize = 25
        message = "I caught a goldfish! It's worth its weight in fish!"
    case 8:
        prize = 50
        message = "You caught a red snapper! It looks pretty dapper!"
    case 9:
        prize = 100
        message = "You caught a blue marlin! Listen to this fish. it's got a point."
    case 10:
        prize = -50
        message = "You fell off!"

print(message, "\nYou've lost: ", prize)


#IPO chart

#Input: Null
#Process: Rng fish
#Output 1: prize/int
#Output 2: message/string
