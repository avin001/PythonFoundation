def most_prolific(input_dict):
    """
    Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
    Write a function most_prolific that takes a dict formatted like Beatles_Discography example above and returns the year in which the most albums were released. If you call the function on the Beatles_Discography it should return 1964, which saw more releases than any other year in the discography.
    """
    work_years = {}
    for key in input_dict:
        if input_dict[key] not in work_years:
            work_years[input_dict[key]] = 1
        else:
            work_years[input_dict[key]] += 1
    num_of_albums = 0
    for year in work_years:
        if work_years[year] > num_of_albums:
            num_of_albums = work_years[year]
            most_prolific_year = year
    return most_prolific_year


Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
print(most_prolific(Beatles_Discography))
