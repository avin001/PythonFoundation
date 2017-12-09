def median(numbers):
    numbers.sort()
    if len(numbers) % 2 != 0:
        return numbers[int(len(numbers) / 2)]
    else:
        return (numbers[int(len(numbers) / 2) - 1] + numbers[int(len(numbers) / 2)]) / 2


print(median([1, 2, 3, 4]))
