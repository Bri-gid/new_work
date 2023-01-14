prompt="Please enter a series of pizza toppings you would like."
prompt+="[Enter 'quit' when you are done.]"
message=" "
while message!='quit':
    message=input(prompt) 
    if message=='quit':
        break
    else:
        print(message.title()+" "+'topping would be added to your pizza.') 

