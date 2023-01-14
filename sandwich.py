def sandwich(*toppings):
	"""listing toppings for a sandwich"""
	print("\nThe following are the list of toppings requested: ")
	for topping in toppings:
		print("-"+ topping.title())

sandwich("beaf","sausage","chicken")

