count = int(4.0)
print(count)
print(type(count))

house_number = 13
street_name = "The Crescent"
town_name = "Belmont"
print(type(house_number))
address = str(house_number) + " " + street_name + ", " + town_name
print(address)

grams_of_sugar = float("35.0")
print(grams_of_sugar)
print(type(grams_of_sugar))

mon_sales = "121"
tue_sales = "105"
wed_sales = "110"
thu_sales = "98"
fri_sales = "95"
total_sales = int(mon_sales) + int(tue_sales) + int(wed_sales) + int(thu_sales) + int(fri_sales)
print("This week's total sales: " + str(total_sales))
