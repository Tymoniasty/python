#numbers

##define and print numeric variable
pi = 3.14159
print(pi)

#calculations
first_num = 6
second_num = 5
print(first_num + second_num)
print(first_num * second_num)
print(second_num-first_num)
print(first_num / second_num)
print(first_num **second_num)

#print mix of string with numbers using + throws an error - can't concatenate different types of variables
#print('five => '+ second_num)

#converting number to string
print('five =>'+str(second_num))
print('five =>',second_num)

#if number saved as a string (within '') concatenate can be confusing:
num_1='1'
num_2='4'
print('1 and 4 with concatenate(+):')
print(num_1+num_2)

#using input to record numbers:
number_1 = input('Whats your first number? ')
number_2 = input('Whats your second number? ')
print('Adding these numbers (input function returns variable as a srting):')
print(number_1+number_2)
print('Treat imput as numbers (either integer or floater):')
print(float(number_1)+int(number_2))