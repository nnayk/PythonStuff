#finger exercise pg 175

def find_ev(list):
    for num in list:
        if num % 2 == 0:
            return num
    raise ValueError("None of the numbers in this list are even")
L = [1, 5, 3, 1]
print(f"The first even number in this list is {find_ev(L)}.")
