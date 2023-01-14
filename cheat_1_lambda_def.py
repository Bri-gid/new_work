'''The lambda returns a value without the return statement.
 It works like the def statement,but there's no need to define it before.'''
#Below prints just "r","g" and "b"

p=list(map(lambda x:x[0],["red","green","blue"]))
print(p)

#Arithmetic example;showing the difference between def and lambda functions

def squares_def(x):
	return(x*x)
a= squares_def(2)
print(a)

squares=lambda x: x*x
print(squares(2))

#the dis keyword shows how both codes works internally
#bytecode instructions for lambda function
import dis
dis.dis(squares)

#bytecode instructions for def funtion
import dis
dis.dis(squares_def)
