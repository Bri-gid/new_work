prompt='Please enter your age: '
prompt+="(Enter a 'negative number' to exit)"
age=input(prompt)
age=int(age)
active=True
while active:
	if age<3 and age>0 :
		print("The ticket is free.")
	elif age>=3 and age<=12:
		print("The ticket is 10cedis.")
	elif age>12:
		print("The ticket is 15cedis.")
	elif age<0:
		break
		

