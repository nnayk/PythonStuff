#factotirla recursion, based on lecture 5 (recursion+dictionaries from mit ocw)

def factorial (a): #b = a-1
    if a == 1:
        return a
    else:
        return a*factorial(a-1)


answer = factorial(5)
print(f"The answer is {answer}")