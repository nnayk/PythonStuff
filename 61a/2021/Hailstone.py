def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    steps=0
    while True:
        print(f'{int(n)}')
        steps += 1
        if n==1:
            break
        if n%2==0:
            n/=2
        else:
            n=3*n+1
    return steps


