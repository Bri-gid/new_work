names=['brigid','pius','aubrey','jessy','erica']
print('The first three names in the list are:')
print(names[:3])
print('Three items from the middle are:')
print(names[1:4])
print('The last three names:')
print(names[2:])




my_pizzas=['veggie','pepperoni','meat','bbq']
friend_pizzas=my_pizzas[:]
friend_pizzas.append('buffalo')
print('My favourite pizzas are:')
for pizza in my_pizzas:
	print(pizza)
print('My friends favourite pizzas are:')
for friend in friend_pizzas:
	print(friend)
	
