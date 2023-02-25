from datetime import datetime
#get current time
today = datetime.now()

#use day,month,year, hour, minute and second functions to display part of the date (no miliseconds)
#Convert to string before concatenating to other string
print('Day: '+str(today.day))
print('Month: '+str(today.month))
print('Year: '+str(today.year))
print('Hour: '+str(today.hour))
print('Minute: '+str(today.minute))
print('Second: '+str(today.minute))

#print('\n Date: ' +str(today.day.month.year))
#print('\n Date: ' +str((today.day)(today.month)(today.year)))
print('\nDate: ' +str(today.day) +str(today.month) +str(today.year))
print('Hour: '+str(today.hour)+':'+str(today.minute)+':'+str(today.second))