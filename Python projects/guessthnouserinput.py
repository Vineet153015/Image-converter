import random

def game(num):
    random_number=random.randint(1,num)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {num} : "))
        if guess > random_number:
            print("No, Guess the samller number")
        elif guess < random_number:
            print("No, Guess the Greater number")
    print(f"Congrats you guessed it right ")

def computer_guess(x):
    low=1
    high=x
    answer =""
    while answer!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        answer = input(f"is {guess} too high(H)? too low(L)? or correct(C)?")
        if answer=='h':
            high=guess-1
        elif answer== 'l':
            low = guess+1
    print(f"congrats computer guessed your number {guess}")


print("Enter the range of the game")
range = input()
game(int(range))

print("Do you want to let computer guess your hidden number?")
choice = input("Y/N? : ")
if choice=='y':
    print("Enter the range to let the computer guess")
    range=input()
    computer_guess(int(range))
else:
    print("Thank you")