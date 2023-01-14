magicians=['aubrey','pius','jessy']
def show_magicians(names):
	'''Prints a list of magicians'''
	print("Below are the list of magicians: ")
	for magician in names:
		print(magician.title())
show_magicians(magicians)
def make_great(magician):
	while magicians:
		name=magicians.pop()
		print(name.title()+" "+"the great")
show_magicians(magicians)
make_great(magicians[:])
		
