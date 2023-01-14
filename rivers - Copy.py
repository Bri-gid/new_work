rivers={
    'amazon': 'brazil',
    'nile': 'egypt',
    'ganges': 'india',
    }
for message,city in rivers.items():
    print("The"+" "+message.title()+" "+ "runs through"+" "+city.title())
for message in rivers.keys():
    print(message.title())
for city in rivers.values():
    print(city.title())

