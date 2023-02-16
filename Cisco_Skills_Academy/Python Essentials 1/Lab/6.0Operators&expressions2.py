# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
# Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ the most important thing is that the code produces valid results for valid input data.
# Test your code carefully. Hint: using the % operator may be the key to success.

hours=int(input("Start time (hours): "))
minutes=int(input("Starting time (minutes): "))
duration=int(input("Duration time (minutes): "))

#calculate hours to minutes
min = hours * 60
#calculate total miuntes (hours in minutes from above) and minutes (from the input)
totalminutes = min + minutes
#add total minutes fom the start time input to duration input
totalendtimeminutes = totalminutes + duration
print("Total minutes (starttime + duration) = ",totalendtimeminutes)
endtimehours = totalendtimeminutes // 60
endtimeminutes = totalendtimeminutes % 60
#if endtimehours > 24
endtimehours=endtimehours%24
print("Endtime hours = ",endtimehours, "Endtime minutes = ", endtimeminutes)
print("End time = ", end="")
print(endtimehours, endtimeminutes,sep=":")

# sample solution:
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# mins = mins + dura # find a total of all minutes
# hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
# mins = mins % 60 # correct minutes to fall in the (0..59) range
# hour = hour % 24 # correct hours to fall in the (0..23) range
# print(hour, ":", mins, sep='')
