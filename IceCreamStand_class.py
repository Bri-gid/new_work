'''An Inheritance project....'''

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
		
class IceCreamStand(Restaurant):
	'''Represents aspect of restaurant,special to the ice cream stand restaurant '''
	def __init__(self,restaurant_name,cuisine_type):
		'''Initialise the attributes of the parent class'''
		'''Initialise attributes specific to the child class'''
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=[]
		
	def describe_flavors(self,*list_flavor):
		"""Printing out the list of flavors available"""
		self.flavors= list_flavor
		print('--THE FOLLOWING ARE THE AVAILABLE FLAVORS--')
		for flavor in self.flavors:
			print('\n'+flavor)
			
'''Making an instance with the flavor method'''
my_icecream=IceCreamStand('biddy',cuisine_type=" ")
my_icecream.describe_flavors('banana','vanilla','strawberry')
			
	
	
