def divisible(n):
    nums = [x for x in range(n+1) if x % 3 == 0 and x % 4 == 0]
    print(nums)
divisible(24)