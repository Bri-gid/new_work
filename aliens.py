#Make an empty list for aliens.
aliens=[]

#Make 30 yellow aliens.
for alien_number in range(30):
	new_alien={"colour":"yellow","speed":"fast","points":10}
	aliens.append(new_alien)

#Printing out the first six aliens
for alien in aliens[:6]:
	print(alien)
print("...")
	
#Shows the total number of aliens.
print("The total number of aliens:"+str(len(aliens)))
