def display_message():
	'''A sentence on what I am learning'''
	print ("I am studying functions.")
display_message()


def favourite_book(title):
	'''something about this book'''
	print(title.title()+" "+"is one of my favourite books.")
favourite_book("sheer cruelty")



def country_city(city,country):
	'''displays a city and its country'''
	home= city + " " + country
	return home.title()
	
motherland=country_city("kumasi","ghana")
print(motherland)


def make_album(artiste_name,album_title,number_of_tracks=" "):
	'''Displays album and artiste name'''
	info={'name':artiste_name,'album':album_title}
	if number_of_tracks:
		info["number_of_tracks"]=number_of_tracks
		return info
musician=make_album('brigid','take me back',55)
print(musician)


def make_album(artiste_name,album_title,number_of_tracks=" "):
	'''Displays album and artiste name'''
	info={'name':artiste_name,'album':album_title}
	if number_of_tracks:
		info["number_of_tracks"]=number_of_tracks
		return info
while True:
	print('Please enter "q" at anytime to quit: ')
	
	name=input('Please enter the name of the artiste: ')
	if name=='q':
		break
		
	title=input('Please enter the title of the album: ')
	if title=='q':
		break
musician= make_album(name,title,55)
print(musician)


magicians=['aubrey','pius','jessy']
def show_magicians(names):
	'''Prints a list of magicians'''
	print("Below are the list of magicians: ")
	for magician in names:
		print(magician.title())
show_magicians(magicians)




magicians=['aubrey','pius','jessy']
modified_magicians=[]
def show_magicians(magician):
	'''modifying the magician list'''
	while magicians:
		current_magician=magicians.pop()
		print("The great"+" "+current_magician)
show_magicians(magicians)



		
		
	



		

