from datetime import datetime, timedelta
#The timedelta object has seven arguments: days, seconds, minutes, hours, weeks, milliseconds, and microseconds.
today = datetime.now()

print('Today is: '+str(today))
#use timedelta to add/remove days/weeks from datetime
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: '+str(yesterday))

#same applies to weeks:
#one_week = timedelta(days=7)
one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: '+str(last_week))