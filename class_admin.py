class Users():
	'''User definition'''
	def __init__(self,first_name,last_name,age,city):
		'''Initialising the variables'''
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.city = city
		
	def describe_user(self):
		'''Prints out a summary of the user profile'''
		print('---USER PROFILE---\n')
		print('First Name: '+self.first_name.title()+'\nLast Name: '+self.last_name.title()+ '\nAge: '+str(self.age)+ '\nCity: '+self.city.title())
		print('\n')
	def greet_user(self):
		'''Greets the user'''
		print('Hello'+ " "+ self.first_name.title() + ' ' + self.last_name.title()+ '!!!')
		
class Admin(Users):
	'''Initialising the parent class variables'''
	'''Initialising the child class variables'''
	def __init__(self,first_name,last_name,age,city):
		super().__init__(first_name,last_name,age,city)
		self.privileges=[]
	
	
	def show_privileges(self,*grants):
		'''This method lists out the privileges of an admin'''
		self.privileges = grants
		print('--ADMIN PRIVILEGES--')
		for privilege in self.privileges:
			print('\n'+privilege)
		
		  
	
		
			
'''Making an instance of the class with the privilege method'''
ad= Admin('brigid','addai-mmra',21,'kumasi')
ad.show_privileges("can add post", "can delete post", "can ban user")


