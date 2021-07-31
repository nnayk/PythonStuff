#finger ex pg 36
num=input("How many times should I print 'X'? ")
counter=0
output=''
while counter<int(num):
    output+='X'
    counter+=1
print(f"Here is the output: {output}. \"X\" was printed a total of {counter} times.")