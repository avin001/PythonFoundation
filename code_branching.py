def garden_calender(season):
    if season == "spring":
        print("Time to plant the garden!")
    elif season == "summer":
        print("Time to water the garden!")
    elif season == "autumn" or season == "fall":
        print("Time to harvest the garden!")
    elif season == "winter":
        print("Time to stay indoors and drink tea!")
    else:
        print("I don't recognize that season.")


garden_calender("summer")
garden_calender("fall")
garden_calender("winter")
garden_calender("rainy")
