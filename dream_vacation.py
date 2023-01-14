responses={}
name=input('Please enter your name: ')
response=input('if you could visit one place in the world,where would you go? ')
poll_active=True
while poll_active:
	responses[name]=response
	repeat=input('Would you like to let another person respond? (yes/no)')
	if repeat=='no':
		poll_active=False
print('---Poll Results---') 
for name,response in responses.items():
	print(name.title()+" "+'would love to visit'+" "+response.title()+".")
