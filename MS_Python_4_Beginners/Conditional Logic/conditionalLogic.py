#Symbols and their oprerations in PYTHON:
# >		Greater than
# <		Less than
# >=	Greater than or equal to
# <=	Less than or equal to
# ==	Is equal to
# !=	Is not equal to

#tax example tax 0.7 for price over 1.00
price = input('Whats the price? ')
#it would be nice to have error handling here for incorrect input (string instead of number)
if float(price) >= 1.00:
   tax = 0.7
   #print(tax)
else:
   tax = 0
print('The tax is '+str(tax))

#string comparision string comparision is case sensitive so the variable needs to use .lower/.upper to ensure it meets the condition
#below the condition won't be true because CANADA is not equal to canada:

	#country = 'CANADA'
	#if country == 'canada':

#to fix above issue use the .lower so the variable is the same as condition
country = input('Where are you from? ')
if country.lower() == 'canada':
	print('You are Canadian')
else:
	print('You are not from Canada! \nYou are from '+country)