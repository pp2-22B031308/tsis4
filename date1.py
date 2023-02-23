import datetime
now = datetime.datetime.now()
now = now - datetime.timedelta(days=5)
print(now.strftime("%D"))