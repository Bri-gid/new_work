class Restaurant():
	'''A restaurant class'''
	def __init__(self, restaurant_name, cuisine_type):
		'''Initialize name and cuisine type'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	
	def describe_restaurant(self):
		'''Prints out the name and the cuisine type'''
		print(self.restaurant_name.title()+ " " + "is the name of the restaurant" + ".")
		print(self.cuisine_type.title()+" "+"is the type of cuisine served here .")
		
		
	def open_restaurant(self):
		'''Prints out an open message'''
		print(self.restaurant_name.title()+"'s" +" "+ "restaurant"+" "+ " is opened!!")
		
