def guess_binary():
    """Return the number of attempted guesses. Implement a faster search
    algorithm that asks the user whether a guess is less than or greater than
    the correct number.

    Hint: If you know the guess is greater than the correct number, then your
    algorithm doesn't need to try numbers that are greater than guess.
    """
    low=1
    high=10
    num_guesses = 1

    inp=""
    closeness=''
    "*** YOUR CODE HERE ***"
    while True:
        guess = (low + high) // 2
        print(f"I think your number is {guess}. ",end='')
        inp=input("Is this correct? ")
        if inp=='y':
            break
        else:
            closeness=input("Is my guess higher (h) or lower (l) than the number? ")
            if closeness=='h':
                high=guess
            else:
                low=guess
        num_guesses+=1
    return num_guesses, guess

count,correct=guess_binary()
print(f'It took me {count} steps to guess the correct value of {correct}')