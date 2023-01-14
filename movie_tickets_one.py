age='Please enter your age: '
age+="(Enter 'a negative number' to exit.)"
age=input(age)
age=int(age)
while age>= 0:
	if age <3:
		print('The ticket is free.')
	elif age==3 or age<=12:
		print('The ticket is 10 cedis.')
	else:
		print ('The ticket is 15 cedis.')
		
	


	

		

