"""A program that reads the content of a file by storing the lines in a list and then working with them outside the with block"""

filename = 'learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()


for line in lines:
	print(line)
