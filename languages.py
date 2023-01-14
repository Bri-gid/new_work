#Making a dictionary of favourite languages.
favourite_languages={
	"brigid":["python","java"],
	"erica":["python","java","c"],
	"danny":["ruby"],
	}
#Looping through the dictionary to print out the list of languages of each person.
for name,languages in favourite_languages.items():
	if len(languages)>1:
		print(name.title()+"'s favourite languages are:")
		for language in languages:
			print(language.title())
	else:
		print(name.title()+"'s favourite language is:")
		for language in languages:
			print(language.title())
			

