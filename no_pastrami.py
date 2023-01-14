sandwich_orders=['chicken','seafood','pastrami','roast beef','grilled cheese','pastrami','ham','nutella','pastrami','grilled chicken']
print('The deli has run out of pastrami.')
while 'pastrami'in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)
