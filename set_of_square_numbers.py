# build a set of all of the square numbers greater than 0 and less than 2,000.
squares = set()
n = 1
while n ** 2 < 2000:
    squares.add(n ** 2)
    n += 1
print(squares)
