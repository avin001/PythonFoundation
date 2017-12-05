given_name = "john william ferrell"
print(given_name.title())
print(given_name.islower())
print(given_name.endswith("ferrell"))
print(given_name.startswith("josh"))
print(given_name.find("william"))
print(given_name.index("john"))
# index() is like find(), but raise ValueError when the substring is not found.
print("ferrell" in given_name)
print("Bob" in given_name)
print(13.37.is_integer())
print(23.0.is_integer())
print("******")
print(given_name[:4])
print(given_name[13:])
print(given_name[-15:-8])
first_name = "john"
print(first_name.capitalize())
print("game".isalpha())
print("game".isdigit())
print("234".isdigit())
print("game234".isalnum())
quote = "Value has a value only if its value is valued."
print(quote.count("value"))
tech_fact = "A tech fact: Java is an object oriented programming language."
tech_fact_lower_case = tech_fact.lower();
vowel_count = tech_fact_lower_case.count("a") + tech_fact_lower_case.count("e") + tech_fact_lower_case.count("i") + tech_fact_lower_case.count("o") + tech_fact_lower_case.count("u")
print(vowel_count)
ip_address = "208.94.117.90"
url = "/bears/koala"
now = "16:20"
log_message = "IP address {} accessed {} at {}".format(ip_address, url, now)
print(log_message)
city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"
alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city, low_temperature, high_temperature, temperature_unit, weather_conditions)
print(alert)
