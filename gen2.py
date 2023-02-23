def even(n):
    for i in range(0, n + 2,2):
        yield i
n = int(input(" "))
num = even(n)
print(','.join(str(x)for x in num))

