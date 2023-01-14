def make_album(artiste,title,number_tracks=""):
	'''Dictionary describing album'''
	album={'name':artiste,'album':title}
	if number_tracks:
		album['number_tracks']=number_tracks
	
	return album
while True:
	print('\nPlease enter the name of your favourite artiste,his/her album,and the number of tracks in the album.')
	print('(enter "q" to quit.)')
#getting info of favorite artiste
	name_artiste=input("artiste name: ")
	if name_artiste=="q":
		break
	the_title=input("title of album: ")
	if the_title=="q":
		break
	the_num_tracks=input("the number of tracks:")
	if the_num_tracks=="q":
		break
	musician=make_album(name_artiste,the_title,the_num_tracks)
	print(musician)
	
    

	
