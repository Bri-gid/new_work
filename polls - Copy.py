responses={}
polling_active=True
#Prompt for name and responds
while polling_active:
	name=input("What is your name? ")
	response=input("Who is your favourite actor? ")

#Get name and responds as key and value of the dictionary responses.
	responses[name]=response
#Get to know if another person wants to take the poll too.
	repeat=input("Do you want someone else to take the poll? yes/no ")
	if repeat=="no":
		polling_active=False
#Polling is finished.Show results.
print("---Polling results---")
for name,response in responses.items():
	print(name.title()+"'s"+" "+"favourite actor is"+" "+response.title()+".")
