def make_pizza(size,*toppings):
	"""summarize the pizza"""
	print("\nMaking a"+" "+str(size)+"- inch pizza with the following toppings:")
	for topping in toppings:
		print("-"+topping)


make_pizza(12,"mushroom","beaf","vegetables")
