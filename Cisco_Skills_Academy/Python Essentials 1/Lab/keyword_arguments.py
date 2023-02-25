#end changes what is sent to the output at the end of the eaguments (by default its '\n')
print("My name is", "Python.", end=" ")
print("Monty Python.")
#sep changes how arguments are separated (by default its a space)
print("My", "name", "is", "Monty", "Python.", sep="-")
#both keyword arguments can be mixed in one invocation:
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
