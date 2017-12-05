def convert_to_numeric(score):
    """
    Convert the score to a numerical type.
    """
    return float(score)


def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    return (score1 + score2 + score3 + score4 + score5) - max(score1, score2, score3, score4, score5) - min(score1, score2, score3, score4, score5)


def score_to_rating_string(score):
    """
    Convert the average score, which should be between 0 and 5, into a string
    """
    if score < 1:
        return "Terrible"
    elif score < 2:
        return "Bad"
    elif score < 3:
        return "OK"
    elif score < 4:
        return "Good"
    else:
        return "Excellent"


def scores_to_rating(score1, score2, score3, score4, score5):
        """
        Turns five scores into a rating by averaging the middle three of the five scores and assigning this average to a written rating
        """
        score1 = convert_to_numeric(score1)
        score2 = convert_to_numeric(score2)
        score3 = convert_to_numeric(score3)
        score4 = convert_to_numeric(score4)
        score5 = convert_to_numeric(score5)

        average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3
        return score_to_rating_string(average_score)


print(scores_to_rating("1", 2, 1.3, "2", 5))
