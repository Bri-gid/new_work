alien_0={"x_position":0,"speed":"medium"}
if alien_0["speed"]=="slow":
	x_increment=1
elif alien_0["speed"]=="medium":
	x_increment=2
else:
	x_increment=3
alien_0["x_position"]=alien_0["x_position"]+x_increment
print("The new position of alien_0 is:"+" "+str(alien_0["x_position"]))

