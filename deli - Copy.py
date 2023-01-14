sandwich_orders=['chicken','seafood','roast beef','grilled cheese','ham','nutella','grilled chicken']#make a list of sandwiches.
finished_sandwiches=[]
while sandwich_orders:
	sandwich=sandwich_orders.pop()
	print('I made you'+" "+ sandwich+ " "+'sandwich'+".")#prints out each sandwich in the list with a message.
	finished_sandwiches.append(sandwich)#each sandwich is transfered into finished_sandwich list as sandwich_orders list is emptied.
print('The following sandwiches have been made:')
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())
	
	
	
