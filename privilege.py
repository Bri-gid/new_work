from userr import Users

class Privileges():
	'''Initializing the class variable'''
	def __init__(self,*privileges):
		self.privileges = privileges
		
	def show_privileges(self,*grants):
		'''This method lists out the privileges of an admin'''
		self.privileges = grants
		print('--ADMIN PRIVILEGES--')
		for privilege in self.privileges:
			print('\n'+privilege)

class Admin(Users):
	'''Initialising the parent class variables'''
	'''Initialising the child class variables'''
	def __init__(self,first_name,last_name,age,city):
		super().__init__(first_name,last_name,age,city)
		self.privileges = Privileges()
