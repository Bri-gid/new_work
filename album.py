def make_album(artiste,title,number_tracks=""):
	'''Dictionary describing album'''
	album={'name':artiste,'album':title}
	if number_tracks:
		album['number_tracks']=number_tracks
	
	return album
music=make_album('lecrea','broken',7)
print(music)
