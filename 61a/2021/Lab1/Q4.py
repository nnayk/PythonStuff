def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    count=0
    length=len(str(n))
    last=0
    sum=0
    while count<length:
        last=n%10
        n//=10
        sum+=last
        count+=1
    return sum