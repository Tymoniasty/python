"""
Create a fill in the blank word game. Prompt the user to enter a noun, verb, and an adjective.
Use those responses to fill in the blanks and display the story.
Write a short story. Remove a noun, verb, and an adjective.
Create a function to get the input from the user.
Create a function that fills in the blanks in the story you created.
Ensure each function contains a docstring.
After the noun, verb, and adjective have been collected from the user, display the story using
their input.
"""
def getnoun():
    """Used to get noun input"""
    noun = input("Please provide a noun: ")
    return noun

def getverb():
    """Used to get verb input"""
    verb = input("Please provide a verb: ")
    return verb

def getadjective():
    """Used to get adjective input"""
    adjective = input("Please provide an adjective: ")
    return adjective

def story(noun, verb, adjective):
    """creates a story"""
    print ("There was a {}. {} liked to {} and was very {}.".format(noun, noun, verb, adjective))

def getwords_and_story():
    """calls both functions to get words and print the story"""
    noun=getnoun()
    verb=getverb()
    adjective=getadjective()
    story(noun, verb, adjective)

getwords_and_story()    
