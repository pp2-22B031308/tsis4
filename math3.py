import math
a = int(input())
b = int(input())
area = ((b**2) * a)/(4*math.tan(math.radians(180/a)))
print(area)