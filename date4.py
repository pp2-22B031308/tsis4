import datetime
x = datetime.datetime(2020, 3, 28, 5, 50, 0)
y = datetime.datetime(2023, 4 , 13, 4 , 4, 0)
diff = (y - x).total_seconds()
print (diff )