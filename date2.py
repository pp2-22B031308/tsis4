import datetime  
x = datetime.date.today()
y = datetime.timedelta(days = 1) + x
z = x - datetime.timedelta(days = 1)
print (z, x, y)