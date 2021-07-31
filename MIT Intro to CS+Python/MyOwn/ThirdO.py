#replace o w q, assume string name = apple: print(apple.replace('o','q')
apple = list(input("Enter a string: "))
ocount = 0
for index in range(len(apple)):
    if apple[index] == 'o':
        ocount += 1
        if ocount % 3 == 0:
            apple[index] = 'q'
print(f"The input with every third \"o\" replaced with a \"q\" is {''.join(apple)}")
#print(apple)