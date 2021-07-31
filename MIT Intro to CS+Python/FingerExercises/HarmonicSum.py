def harm_sum(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return 1/num + harm_sum(num-1)
#number = int(input("Enter a number: "))
sum = harm_sum(int(input("Enter a number: ")))
print(f"The sum is {sum}.")