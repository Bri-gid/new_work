class Users():
	'''User instance'''
	def __init__(self,first_name,last_name,age,city):
		'''Initialising the variables'''
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.city = city
		self.login_attempts = 0
		
		
	def describe_user(self):
		'''Prints out a summary of the user profile'''
		print('---USER PROFILE---\n')
		print('First Name: '+self.first_name.title()+'\nLast Name: '+self.last_name.title()+ '\nAge: '+str(self.age)+ '\nCity: '+self.city.title())
		print('\n')
		
		
	def greet_user(self):
		'''Greets the user'''
		print('Hello'+ " "+ self.first_name.title() + ' ' + self.last_name.title()+ '!!!')
		
	
	def increment_login_attempts(self,login_attempt):
		'''Increases the login attempts by 1'''
		self.login_attempts = login_attempt + 1
		print(str(self.login_attempts)+ " " + "login attempts.")
		
	
	def reset_login_attempts(self):
		'''Resets the login_attempts to zero'''
		self.login_attempts = 0
		print(str(self.login_attempts))
		print("The number of login attempts has been reseted to zero(0).")
		
'''Calling the increament method'''
user= Users('brigid','addai-mmra',21,'kumasi')
user.increment_login_attempts(2)
		
'''Calling the reset method'''
user.reset_login_attempts()
	


	
