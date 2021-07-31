import random
def guess_function():
    print("Pick a number from 1-10 and I will guess it.")

    correct=False
    inp='n'

    guess=0
    guessed=[]


    while not correct and len(guessed)!=10:
        guess=random.randint(1,10)
        while guess in guessed:
            guess=random.randint(1,10)
        guessed.append(guess)
        print("I think the number is",str(guess)+". ",end='')
        inp=input("Is this correct? ")
        if inp=='y':
            correct=True
            print("Your number was",guess)
            return
    print("Sorry, your number is not within the range 1-10")

guess_function()

