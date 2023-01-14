'''A program that prints the content of a file by looping over the file object'''
filename='learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.strip())
