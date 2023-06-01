import random

def game(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x} : "))
        if guess < random_number:
            print("No,Guess the Greater Number")
        elif guess > random_number:
            print("No, Guess the smaller nummber")
    print(f"Congrats you have guessed it right the number is : {random_number}")


def computer_guess(x):
    low=1
    high=x
    answer=""
    while answer!='c':
        if low !=high:
            guess = random.randint(low,high)
        else:
            guess = low
        answer=input(f"is {guess} too high(H)?,too low(L) or correct(C)? : ")
        if answer=='h':
            high = guess-1
        elif answer == 'l':
            low = guess+1
    print(f"Computer gueesed your number ,{guess}")

game(20)
computer_guess(10)