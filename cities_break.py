prompt="Which cities would you like to visit?"
prompt+="(Please enter 'quit'when you are done.) "
active=True
while active:
	message=input(prompt)
	if message=='quit':
		break
	else:
		print("I would like to visit"+" "+message.title()+".")
	
