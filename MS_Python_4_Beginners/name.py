#define variables
# first_name='Lukas'
# last_name='Tymczak'
first_name = input('Whats your name? ')
last_name = input ('Whats your last name? ')
#print firstname
print(first_name)
#print text and variables with  as a connector
print('Hello' + first_name + last_name)
#print text and variables with coma as a connector
print('Hello',first_name,last_name)
#print with capitalised names
print('Hi',first_name.capitalize(),last_name.capitalize())
#testing output with place holders and format
output = 'Hello, {} {}'.format(first_name,last_name)
print(output)
#testing output with different order space between placeholders {}
output = 'Hello, {1} {0}'.format(first_name,last_name)
print(output)
#testing formating (available only on Python3) no spaces between variables in placeholders {}
output = f'Hello, {first_name}{last_name}'
print(output)
#testing placeholder with capitalised names
output = f'Hello, {first_name.capitalize()} {last_name.capitalize()}'
print(output)
output = 'Hello, {1} {0}'.format(first_name.capitalize(),last_name.capitalize())
print(output)