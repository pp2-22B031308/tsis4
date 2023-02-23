import datetime
now = datetime.datetime.now()
print(f"Without Microseconds - {now.strftime('%Y-%m-%d %H:%M:%S')}")
now=datetime.datetime.now()
now2=now.replace(microsecond=0)
print (now2)
print (now )
