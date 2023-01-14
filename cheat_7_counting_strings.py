text='Have a nice day'
# space count counts the spaces in between the words
space_count=text.count(' ')
total_count=len(text)
#Counts the number of the character a in the text and prints it out
total_a=text.count('a')
print(total_a)
print(space_count)
#Prints False because the length of the spaces and the length are not the same
print(space_count==total_count)
