#pg 72 finger exercise

def mult(first,second=None):
    if second == None:
        print(f"Only one integer was given: {first}")
    else:
        print(f"The product of the two integers is {first*second}")
#mult(first=3)
#mult(3)
#mult(first=9,second=6)