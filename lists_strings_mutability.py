sample_string = "And Now For Something Completely Different"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
print(sample_string[4])
print(sample_list[4])
print(sample_string[12:21])
print(sample_list[2:4])
print(len(sample_string))
print(len(sample_list))
print('thing' in sample_string)
print('morning' in sample_string)
print('Rowan' in sample_list)
print('John' in sample_list)
sample_list[4] = 'Avin'
print(sample_list)
# sample_string[8] = 'f'
# if the above commented line is uncommented and run we get the following error
# TypeError: 'str' object does not support item assignment
# Lists are mutable, while strings are immutable
sample_list[0:2] = ['Paul', 'Tiffany']
print(sample_list)
