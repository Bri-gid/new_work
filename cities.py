cities={
    'paris':{
        'country':'France',
        'populations':'2,183,055million',
        'facts':'has zero STOP signs for cars.',
        },
    'mexico city':{
        'country':'mexico',
        'populations':'21.7million',
        'facts':'is built on a lake called Texacoco which continuously makes the city sink.',
        },
    'athens':{
        'country':'Greece',
        'populations':'3,153,000',
        'facts':"has one of the lowest crime rates in all of Europe's major cities.",
        },
    }    
for city,facts in cities.items():
    print (city.title())
    for fact in facts.items():
        print(fact)
    
