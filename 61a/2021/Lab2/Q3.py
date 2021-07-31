#curry lambda expression
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x,y)

def add(x,y):
    return x+y
fun=lambda_curry2(add)
adder=fun(3)
add_three=adder(5)
print(f'add_three={add_three}')