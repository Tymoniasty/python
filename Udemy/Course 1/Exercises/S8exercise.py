# Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and their interesting fact to the screen. Next, change a fact about one of
# the people. Also add an additional person and corresponding fact. Display the new list of people
# and facts. Run the program multiple times and notice if the order changes.

# peoplefacts={'Jeff':'Is afraid of heights',
#              'David':"Plays the piano",
#              'Jason':'Can fly an airplane',
#              'Jill':'Can hula dance'}
# for person in peoplefacts:
#     print("{0}: {1}.".format(person, peoplefacts[person]))

#Solution:
def display_facts(facts):
    '''Displays output of the dictionary'''
    for fact in facts:
        print("{} : {}.".format(fact, facts[fact]))
    print()
#create dictionary  
facts={
    'Jason':'Can fly an airplane',
    'Jeff':'Is addraid of clowns',
    'David':'Plays the piano'
}
#call the function to display the initial dictionary
display_facts(facts)

#amend dictionary
facts['Jeff'] = 'Is afraid of heights'
facts['Jill'] = 'Can hula dance'

#display updated dictionary
display_facts(facts)