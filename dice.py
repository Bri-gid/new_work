from random import randint

class Die():
	'''Making a die which generates random numbers'''
	
	def __init__(self,sides=6):
		'''Initialising the dice attribute'''
		self.sides=sides
		
		
	def roll_die(self):
		'''Prints a random number between 1 and the sides the die has'''
		roll = randint(1,self.sides)
		print(roll)
		
		

my_dice=Die(20)
my_dice.roll_die()
	
		
		
		


	
