# For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code
with open('/Users/avin001/PythonFoundation/PythonFoundationNanodegree/DataScientist.txt') as f:
    for line in f:
        print(line, end='')

list_of_lines_in_file = []
with open('/Users/avin001/PythonFoundation/PythonFoundationNanodegree/DataScientist.txt') as f:
    for line in f:
        list_of_lines_in_file.append(line.strip())
print('\n\n\n\n')
print(list_of_lines_in_file)
