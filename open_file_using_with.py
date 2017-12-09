# Python allows you to open a file, do operations on it, and automatically close it afterwards using with.

with open('/Users/avin001/PythonFoundation/PythonFoundationNanodegree/MyFirstWithUdacity.txt', 'r') as f:
    file_data = f.read()
print(file_data)
