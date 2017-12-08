def check_answer(answer, solution):
    """
    Checks the answer to the solution and returns True or False
    answer: answer as string
    solution: solution as string
    """
    if answer == solution:
        return True
    else:
        return False


def evaluate_result(my_answers, solutions):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    my_answers: list of answers provided by user
    solutions: list of correct answers
    """
    results = [None, None, None, None, None]
    for x in range(len(results)):
        results[x] = check_answer(my_answers[x], solutions[x])
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        else:
            count_incorrect += 1
    if count_correct / 5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect / 5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."


print(evaluate_result(['Blue', '7', 'East', 'Japanese', 'Japan'], ['Blue', '7', 'East', 'Japanese', 'Japan']))
