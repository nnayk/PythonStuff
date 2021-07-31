#finger exercise pg 49
integer=int(input("Enter an integer: "))
pair_exists=False
for root in range(1,integer):
    for power in range(1,7):
        if root**power==integer:
            print(f"{root}^{power}={integer}")
            pair_exists=True
        elif root==integer-1 and power==6 and pair_exists==False:
            print(f"Sorry, there is no combination of numbers such that a number <{integer} raised to a power from"
                  f" 1-6 ={integer}")