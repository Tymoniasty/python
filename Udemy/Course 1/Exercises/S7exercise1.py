# Create a Python program that captures and displays a person's to­do list. 
# Continually prompt the user for another item until they enter a blank item. 
# After all the items are entered, display the
# to­do list back to the user.

#creating an empty list
todolist = []

#first question
task=input("What would you like to add to the 'To Do' List?: Please press <enter> when ready: " )
todolist.append(task)
#while loop to gather tasks from the user
while  task !="":
    task=input("What would you like to add to the 'To Do' List?: Please press <enter> when ready: " )
    todolist.append(task)

#print the task list
print()
header="Your 'To Do' list is as follow: "
print(header)
print('-'* len(header))
#variable for task numbers 'i'
i=1
for t in todolist:
    if t!="":
        print(str(i),". ", end=" ")
        print(t)
        i+=1
print()
#the above with while  loop

#variable for list index 'index'
#index=0
# while index<len(todolist):
#     print(str(i),". ", end=" ")
#     print(todolist[index])
#     i+=1
#     index+=1

#debug print list
#print(todolist)

#Solution:

# to_do_list = []
# finished = False

# while not finished:
#     task = input('Enter a task for your to-do list. Press <enter> when done: ')
#         if len(task) == 0:
#             finished = True
#         else:
#             to_do_list.append(task)
#             print('Task added.')

# # Display the to-do list.
# print()
# print('Your To-Do List:')
# print('-' * 16)
# for task in to_do_list:
#     print(task)