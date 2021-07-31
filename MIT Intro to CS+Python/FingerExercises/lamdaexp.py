#pg 85 finger exercise
def find_val (val_1,val_2):
        return lambda val_1, val_2: val_1*val_2

first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
if second == 0:
    print(None)
else:
    value = find_val(first,second)
    print(value(first,second))


