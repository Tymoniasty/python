# # Write a Python program that prompts for input and displays a cat "saying" what was provided by
# the user. Place the input provided by the user inside a speech bubble. Make the speech bubble
# expand or contract to fit around the input provided by the user.

text_input = input('Please type something and press enter: ')
text_input_len = len(text_input)
print('          {}'.format('_'*text_input_len))
print('         <{}>'.format(text_input))
print('          {}'.format('-'*text_input_len))
print('           /')
print(' /\_/\    /')
print('( o.o )')
print(' > ^ <')