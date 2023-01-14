motorcycles=["honda","yamaha","suzuki","ducati"]
print(motorcycles)
too_expensive="ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA"+" "+ too_expensive+" " +" is too expensive.")
del motorcycles[0]
print(motorcycles)
motorcycles.insert(0,"hunda")
print(motorcycles)
popped=motorcycles.pop()
print(popped)


integers=[1,5,3,4,2,8,9]
integers.sort()
print(integers)
integers.sort(reverse=True)
print(integers)
print(sorted(integers))
print(sorted(integers,reverse=True))


squares=[value**2 for value in range(1,11)]
print(squares)


numbers=[number**1 for number in range(1,21)]
print(numbers)


odd=[num*1 for num in range(1,11,2)]
print(odd)


multiple_of_three=[multiple*3 for multiple in range(1,11)]
print(multiple_of_three)


cube=[]
for num in range(1,11):
	cube.append(num**3)
print(cube)


multiple=[num**3 for num in range(1,11)]
print(multiple)



favourite_books={
	"brigid":"pride and prejudice",
	"aubrey":"things fall apart",
	}
friends=["aubrey","pius"]
for name in favourite_books:
	print(name.title())
	if name in friends:
		print("Hi" +" "+ name.title()+" " +"I see your favourite book is"+
		" " +favourite_books[name].title()+ "!")
		
		
favourite_language={
	"biddy":"spanish",
	"aubrey":"italiano",
	"jessy":"french",
	"pius":"twi",
	}
for name in sorted(favourite_language.keys(),reverse=True):
	print(name.title()+" , thank you for taking the poll.")
			

		
		
	
		






