import random
#
def logic(user):
     #log = dict(r = 'rock', )
    log=[1,2,3,4]
    val = 0
    log[val] = int(random.randint(0,3))
    if log[0] and  (user == 'rock'):
        print("rock & rock it's a draw")
    elif log[0] and ( user == 'scissors'):
        print("rock trumps scissors , you've being decimated")
    elif log[0] and ( user == 'paper'):
        print("rock is no match for paper , you got them covered")

    #if computer picks paper
    elif  log[1] and (user == 'rock'):
        print("paper trumps rock, you are covered")
    elif  log[1] and (user == 'scissors'):
        print('scissors shreds paper, They"ve being decimated')
    elif  log[1] and (user == 'paper'):
        print("paper & paper, it's a Draw")


    #if computer picks scissors
    elif  log[2] and (user == 'rock'):
        print("They've been decimated, rock wins")
    elif  log[2] and (user == 'scissors'):
        print("We have ourselves a standoff, a draw ")
    elif  log[2] and (user == 'paper'):
        print("You've shredded the paper well to shreds")
    else:
        pass

    

def main():
    print("you are playing rock paper scissors /n")
    user = input(" 'r' for rock, p for paper, s for Scissors ")

    playerinput = dict(r = 'rock', p = 'paper', s = 'scissors')
 
    if user in playerinput:
        print(playerinput[user])
        logic(playerinput[user])
    
    elif user not in playerinput:
        raise ValueError('use letter r , p, or s')







if __name__ == "__main__" : main()