biddy={'first_name':'brigid','last_name':'addai-mmra','age':'20','city':'kumasi'}
jessy={'first_name':'jessy','last_name':'abrafi','age':'15','city':'kumasi'}
pius={'first_name':'pius','last_name':'twumasi','age':'24','city':'kumasi'}
people=[biddy,jessy,pius]
for person in people:
    for name,info in person.items():
        print(name.title())
        print(info.title())
