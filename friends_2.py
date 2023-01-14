favourite_language={
	"erica":"python",
	"brigid":"c",
	"danny":"ruby",
	"gideon":"java",
	}
friends=["erica","brigid"]
for name in sorted(favourite_language.keys()):
	if name in friends:
		print("Hi"+" "+name.title()+" "+"I see your favourite language is"+" "+favourite_language[name].title()+".") 
	else:
		print(name.title())
	
	

