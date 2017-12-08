elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}

# This dictionary maps element names (strings) to their atomic numbers (ints). But what if we wanted to store more information about each element, like their weight and symbol? We can do that by adjusting the dictionary so that it maps element names (strings) to a dictionary that stores that collection of data:

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'}, 'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

print(elements['helium'])
print(elements.get('unobtainium', 'There\'s no such element!'))
print(elements.get('hydrogen'))
print(elements['hydrogen']['weight'])
