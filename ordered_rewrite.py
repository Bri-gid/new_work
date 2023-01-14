from collections import OrderedDict 

"""This program uses orderedDict from collections in
 standard library to order the key and value """
 
glossary = OrderedDict()

glossary['list'] = ':List is a data structure in python that is mutable,ordered sequence of elements.'
glossary['tuple'] = ':Tuple is a data structure in python that is immutable,ordered sequence of elements.'
glossary['append'] = ':append() in python adds a single element to an existing list.'
glossary['sorted'] = ':sorted() funtion returns a sorted list from the iterable object.'
glossary['del'] = ':del keyword in python is primarily used to delete objects in python.'

for name,definition in glossary.items():
	print(name.title()+ " "+ definition)
