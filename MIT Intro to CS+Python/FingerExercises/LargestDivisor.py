#finger exercise pg 49
number=int(input("Please enter an integer: "))
largest_divisor=None
for divisor in range(3,number):
    if number%divisor==0:
        largest_divisor=divisor
if largest_divisor!=None:
    print(f"{number} is not a prime number. Its largest divisor is {largest_divisor}")
else:
    print(f"{number} is a prime number.")