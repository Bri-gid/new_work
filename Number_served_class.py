class Restaurant():
	'''A restaurant class'''
	def __init__(self, restaurant_name, cuisine_type):
		'''Initialize name and cuisine type'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served=0
		
	
	def describe_restaurant(self):
		'''Prints out the name and the cuisine type'''
		print(self.restaurant_name.title()+ " " + "is the name of the restaurant" + ".")
		print(self.cuisine_type.title()+" "+"is the type of cuisine served here .")
		if self.number_served > 1:
			print(str(self.number_served)+ ' ' + 'number of people have been served.')
		else:
			print(str(self.number_served) +' '+ 'person has been served.')
		
		
		
	def open_restaurant(self):
		'''Prints out an open message'''
		print(self.restaurant_name.title()+"'s" +" "+ "restaurant"+" "+ " is opened!!")
		
		
	def set_number_served(self,served_customers):
		'''setting numbers of customers served through a method'''
		self.number_served = served_customers
	
	def increment_number_served(self,increase):
		'''Adding new customers served to the previous'''
		self.number_served += increase
				

		
'''Making an instance of the class'''
my_restaurant= Restaurant('brigid','chinese')
my_restaurant.set_number_served(44)
my_restaurant.increment_number_served(22)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(44)



