def population_density(population, land_area):
    """Calculate the population density of an area

    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass in value in terms of square km or square miles the function will return a density in those units.
    """
    return population / land_area


test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected_result: {}, actual result: {}".format(expected_result2, test2))

# return_value = print("Trying to print return value of a print function")
# print(return_value)


def print_testcase(expected_value, actual_value):
    print("expected value: {}, actual value: {}".format(expected_value, actual_value))


return_value = print_testcase(42, 42)
print(return_value)
