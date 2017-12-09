AngkorWat = (13.4125, 108.866667)
print(type(AngkorWat))
print("AngkorWat is at latitude: {}".format(AngkorWat[0]))
print("AngkorWat is at longtitude: {}".format(AngkorWat[1]))

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
length, width, height = 52, 40, 100 # tuple unpacking
# tuple immutability makes a case for tuples to be stored in sets or used as the keys of a dictionary
world_heritage_locations = {(13.4125, 108.866667): "Angkor Wat", (25.73333, 32.6): "Ancient Thebes", (30.330556, 35.4433330): "Petra", (-13.116667, -72.583333): "Machu Picchu"}
# A common use for tuples is to return multiple values from a function
def first_and_last(sequence):
    """returns the first and last elements of a sequence"""
    return sequence[0], sequence[-1]


print(first_and_last(["Spam", "egg", "sausage", "Spam"]))
# A function that returns multiple values can also be used to assin multiple variables
start, end = first_and_last(["Spam", "egg", "sausage", "Spam"])
print(start)
print(end)
