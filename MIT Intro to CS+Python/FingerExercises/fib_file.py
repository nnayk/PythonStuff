def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for call in range(0,10):
    value = fib(call)
    #with open('fibby','w') as han:
     #   han.write('hallo')
    file_han = open('fibby','a')
    file_han.write(f"{value}\n")
    #file_han.writelines(["a","b"])
    file_han.close()
with open('fibby','r') as file_han:
    print(file_han.read())
