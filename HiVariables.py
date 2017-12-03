manila_pop = 1780148
print(manila_pop)
manila_area = 16.56
manila_pop_density = manila_pop / manila_area
print(manila_pop_density)
manila_pop = 1781573
print(manila_pop)
manila_pop = manila_pop + 1675 - 250
print(manila_pop)
x = 2
x += 4
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)

# The current volume of a water reservoir (in cubic metres)
# Note that this code uses scientific notation to define large numbers.
# 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= (rainfall * 0.1)

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume += (reservoir_volume * 0.05)

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= (reservoir_volume * 0.05)

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)
