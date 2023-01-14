favourite_language={
	"erica":"python",
	"brigid":"c",
	"danny":"ruby",
	"gideon":"java",
	}
friends=["erica","brigid"]
for name in favourite_language.keys():
	print(name.title())
	
	if name in friends:
		print("Hi"+" "+name.title()+" "+"I see your favourite language is"+" "+favourite_language[name].title()+".") 

