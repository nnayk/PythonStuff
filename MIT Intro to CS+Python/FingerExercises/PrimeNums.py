# finger exercise pg.40
# print sum of prime numbers greater than 2 and less than 1000
sum=0
for num in range(3,1000):
    div_count=0 # div_count is the number of divisors for the number (should be =2 for prime numbers)
    for divisor in range(1,1000):
        if num%divisor==0:
            div_count+=1
        if div_count==2 and divisor==999:
            sum+=num
print(f"The sum of the prime numbers >2 and <1000 is {sum}")