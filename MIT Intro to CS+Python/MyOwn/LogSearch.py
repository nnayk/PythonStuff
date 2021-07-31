#pg 222 guttag program
def int_to_str (i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10]+result
        i = i // 10
    return result
number = 56
value = int_to_str(number)
print(f"The string representation of this number is " + value)