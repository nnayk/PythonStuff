#testing out prof guttag's cube root program on pg 45 bc i think theres an error (seems like there will be
#unnecessary printing of "$x is not a perfect cube"

x=int(input("Enter an integer: "))
ans=0
while ans**3<abs(x):
    ans=ans+1
if ans**3!=abs(x):
    print(f'{x} is not a perfect cube')
else:
    if x<0:
        ans=-ans
    print(f"Cube root of {x} is {ans}")