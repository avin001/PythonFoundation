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


def which_prize(points):
    if 0 <= points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif 51 <= points <= 150:
        return "Oh dear, no prize this time."
    elif 151 <= points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    elif 181 <= points <= 200:
        return "Congratulations! You have won a penguin!"


print(which_prize(12))


def punctuate(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create.
                 "exclamation", "question" and "aside" are known values.
    """
    if phrase_type == "exclamation":
        sentence_punct = sentence + "!"
    elif phrase_type == "question":
        sentence_punct = sentence + "?"
    elif phrase_type == "aside":
        sentence_punct = "(" + sentence + ".)"
    else:
        sentence_punct = sentence + "."
    return sentence_punct


print(punctuate("How's the course going so far", "question"))


def punctuate2(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create.
                 "exclamation", "question" and "aside" are known values.
    """
    if phrase_type == "exclamation":
        return sentence + "!"
    elif phrase_type == "question":
        return sentence + "?"
    elif phrase_type == "aside":
        return "(" + sentence + ".)"
    else:
        return sentence + "."


print(punctuate2("Let's see how far you've reached in the course", "aside"))


def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return 2 * top_area + side_area
    else:
        return side_area


print(cylinder_surface_area(10, 20, True))
print(cylinder_surface_area(10, 20, False))

errors = 3
if errors:
    print("There are " + str(errors) + " mistakes. Please correct.")
else:
    print("No mistakes here!")


def which_prize2(points):
    prize = None
    if 0 <= points <= 50:
        prize = "a wooden rabbit"
    elif 51 <= points <= 150:
        prize = None
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif 181 <= points <= 200:
        prize = "a penguin"

    if prize:
        return "Congratulations! You have won {}!".format(prize)
    else:
        return "Oh dear, no prize this time."


print(which_prize2(12))
