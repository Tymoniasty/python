#to use current date/time we need to use the 'datetime' library
from datetime import datetime

current_date = datetime.now()
#now() returns current date and time

#print('Today is: ' + current_date)
#the above throws an err - you need to convert to string before concatenate into text
print('Today is: ' + str(current_date))