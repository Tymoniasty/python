#Create a for loop that counts from 0 to 10, and prints odd numbers to the screen.
for i in range(1,11):
    while i % 2 != 0:
        print(i)
        i+=1
print("Answer:")
for i in range(0, 11):
    if i % 2 != 0:
        print(i)