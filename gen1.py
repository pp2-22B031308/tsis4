def square(n):
    for i in range(1, n+1):
        yield i *i 
for number in square(7): 
    print (number)