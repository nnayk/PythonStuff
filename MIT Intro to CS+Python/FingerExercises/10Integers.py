#finger ex pg 36
list=[]
for counter in range(1,11):
    num=int(input(f"Enter number {counter}: "))
    if num % 2 != 0:
        list.append(num)
    counter+=1

if len(list) > 0:
    print("The maximum odd number that you entered is "+str(max(list)))
else:
    print("You did not enter any odd numbers.")