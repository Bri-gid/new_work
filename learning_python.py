'''A program that reads a file and prints the content'''

filename = 'learning_python.txt'
with open (filename) as file_object:
	for line in file_object:
		print(line.strip())
		

		

	
