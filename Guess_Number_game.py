# Guess the number !
import simplegui
import random

# global variables
secret_number = 0
rang = 0 
attempts = 7

#helper function
def compare(guess):
    global secret_number 
    if(secret_number == guess):
        print "Correct !"
    elif (secret_number < guess):
        print "Higher!"
    else :   
        print "Lower!"

def range_1():
    global rang, attempts
    rang, attempts = 100, 7
    new_game()

def range_2():
    global rang, attempts
    rang, attempts = 1000, 7
    new_game()

def new_game():
    global secret_number, rang, attempts
    secret_number = random.randrange(0, rang)
    print "\nNew Game : Selected range 0 -", rang
    print "Attempts remaining : ", attempts

#input handler
def input_guess(guess ):
    global secret_number, attempts
    guess = int(guess)
    if(attempts != 0) :
        print "\nGuess was ", guess
        compare(guess)
        attempts -= 1
        if(attempts == 0):
            print "Attempts remaining : ", attempts, "Restart Game , Select Range"
        else:
            print "Attempts remaining : ", attempts
    else :
        print "Attempts remaining : ", attempts," You loose the game, Restart Game"
    
# frame 
frame = simplegui.create_frame("Guess_number", 200, 200)
range_button_1 = frame.add_button("0 - 100", range_1,100)
range_button_2 = frame.add_button("0 - 1000", range_2, 100)
ip = frame.add_input("number", input_guess, 100) 

#start
frame.start()