'''This program opens the pi_digits.txt file,reads it,and prints the contents of the file on a screen'''

with open('pi_digits.txt')as file_object:
	contents = file_object.read()
	print(contents)
