def count_change(amount,start_coin=16):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    if amount==0:
        return 1

    elif amount<0:
        return 0

    elif start_coin==0:
        return 0

    else:
        return count_change(amount-start_coin,start_coin)+count_change(amount,start_coin//2)
