#Make an empty list to later hold the odd numbers
odd_numbers=[]
current_number=0
while current_number<10:
	current_number+=1
	
#if current number is divisible by 2,the program continues to the next number
	if current_number%2==0:
		continue
	odd_numbers.append(current_number)
print(odd_numbers)
