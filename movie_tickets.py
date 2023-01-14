age=input('Please enter your age: ')
age=int(age)
if age<3:
	print('The ticket is free.')
elif age==3 or age<=12:
	print('The ticket is 10 cedis.')
else:
	print('The ticket is 15 cedis.')
	
