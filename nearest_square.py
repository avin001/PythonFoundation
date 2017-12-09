def nearest_square(limit):
    num = 1
    while num**2 < limit:
        num = num + 1
    return (num - 1)**2


test1 = nearest_square(40)
print("Expected result: 36, Actual result: {}".format(test1))
