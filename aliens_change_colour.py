#Make an empty list for aliens.
aliens=[]

#Make 30 yellow aliens.
for alien_number in range(30):
	new_alien={"colour":"yellow","speed":"fast","points":10}
	aliens.append(new_alien)

#Printing out the first six aliens in green
for alien in aliens[:6]:
	if alien["colour"]=="yellow":
		alien["colour"]="green"
		alien["speed"]="slow"
		alien["points"]=5
		
for alien in aliens[:9]:
	print(alien)
print("...")
	
#Shows the total number of aliens.
print("The total number of aliens:"+str(len(aliens)))

