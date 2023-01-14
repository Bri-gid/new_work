def car(manufacturer,model,**car_info):
	"""summary on a car"""
	car_profile={}
	car_profile["manufacturer_name"]=manufacturer
	car_profile["model_name"]=model
	for key,value in car_info.items():
		car_profile[key]=value
	return car_profile
build_car=car("Elon Musk","Tesla",location="Texas",date="1-01-2001")
print(build_car)

 
