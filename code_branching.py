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

phone_balance = 7.62
bank_balance = 104.39
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
print(phone_balance)
print(bank_balance)


number = 145346334
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")

age = 35
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65
concession_ticket = 1.25
adult_ticket = 2.50
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)
