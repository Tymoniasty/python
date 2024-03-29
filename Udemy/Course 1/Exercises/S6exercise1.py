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

# def get_word(word_type):
#     """Get a word from a user and return that word."""
#     # The lower() function converts the string to lowercase before testing it
#     if word_type.lower() == 'adjective':
#     # Use 'an' in front of 'adjective'
#        a_or_an = 'an'
#     else:
#     # Otherwise, use 'a' in front of 'noun' or 'verb'
#         a_or_an = 'a'
#     return input('Enter a word that is {0} {1}: '.format(a_or_an, word_type))

# def fill_in_the_blanks(noun, verb, adjective):
#     """Fills in the blanks and returns a completed story."""
#     # The \ lets the string continue on the next line to make the code easier to read
#     story = "In this course you will learn how to {1}. " \
#             "It's so easy even a {0} can do it. " \
#             "Trust me, it will be very {2}.".format(noun, verb, adjective)
#     return story

# def display_story(story):
#   """Displays a story."""
#   print()
#   print('Here is the story you created. Enjoy!')
#   print()
#   print(story)

# def create_story():
#   """Creates a story by capturing the input and displaying a finished story."""
#   noun = get_word('noun')
#   verb = get_word('verb')
#   adjective = get_word('adjective')

#   the_story = fill_in_the_blanks(noun, verb, adjective)
#   display_story(the_story)

# create_story()