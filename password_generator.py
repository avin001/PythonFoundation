import random

word_file = "words.txt"
word_list = []

with open(word_file, 'r') as words:
    for line in words:
        word = line.strip().lower()
        if 3 < len(word) < 8:
            word_list.append(word)


def generate_password(input_list):
    password = ''
    for i in range(3):
        password += input_list[random.randint(0, len(input_list) - 1)]
    return password


print(generate_password(word_list))
