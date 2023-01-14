names=['phyte','asumadu','godfred','punch']
print(names[0].title())
print(names[1].title())
print(names[-2].upper())
print(names[-1].lower())

greetings="Hello,how are you doing"
print(greetings+" "+names[0].upper())
print(greetings+" "+names[1].upper())
print(greetings+" "+names[2].upper())
print(greetings+" "+names[3].upper())

cars=['tesla','benz','range rover','rav4']
message="i'd love to own a"
print(message+" "+cars[0].upper()+" "+"someday.")


names=['brigid','biddy','addai-mmra']
popped_names=names.pop()
print(names)
print(popped_names)
