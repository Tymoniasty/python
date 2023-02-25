"""
Create a program that asks the user how far they want to travel. If they want to travel less than
three miles tell them to walk. If they want to travel more than three miles, but less than three
hundred miles, tell them to drive. If they want to travel three hundred miles or more tell them to
fly.
Sample Output:
How far would you like to travel in miles? 2500
I suggest flying to your destination.
"""

distance=int(input("How far do you wish to travel? "))
if distance <= 3:
    print("You can walk!")
elif distance>3 and distance<300:
    print("You can drive!")
else:
    print("You should fly!")

"""
# Ask for the distance.
distance = input('How far would you like to travel in miles? ')
# Convert the distance to an integer.
distance = int(distance)
# Determine what mode of transport to use.
if distance < 3:
mode_of_transport = 'walking'
elif distance < 300:
mode_of_transport = 'driving'
else:
mode_of_transport = 'flying'
# Display the result.
print('I suggest {} to your destination.'.format(mode_of_transport))
"""    
