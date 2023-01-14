gradings=[]
gradings_active=True
while gradings_active:
	exam=int(input("Please enter your exam score: "))
	midsem=int(input("Please enter you midsem score :"))
	exams=(exam/100)*70
	midsems=(midsem/100)*30
	total=exams + midsems
	gradings.append(total)
	for grade in gradings:
		if grade>=70:
			print("You had an A and you result is: "+ str(grade))
		elif grade>=60:
			print("You had a B and your result is: "+ str(grade))
		elif grade>=50:
			print("You had a C and your result is: "+ str(grade))
		elif grade >= 40:
			print("You had a D and your result is: "+ str(grade))
		else:
			print("You had an F and your result is: "+ str(grade))
		repeat=input("Are you done with the grading? yes/no: ")
		if repeat=="yes":
			gradings_active=False
print(str(max(gradings))+ "is the maximum number.")
			
	


	
		
	
		
	
		
	
		
	
		

