f = open('/Users/avin001/PythonFoundation/PythonFoundationNanodegree/MyNextWithUdacity.txt', 'w')
# Caution: once you open a file in writing mode, anything that it had contained previously will be deleted. If you're interested in adding to an existing file (without deleting its content) you should use append instead of write and open in append mode (using a instead of w).
f.write("I plan to pursue 'Data Analyst Foundation Nanodegree' program from Udacity after completing 'Python Foundation Nanodegree' program. It involves mastering data fundamentals applicable to any industry, and learn to make data-driven decisions. Learn Excel and SQL, and gain data visualization skills with Tableau.")
f.close()
