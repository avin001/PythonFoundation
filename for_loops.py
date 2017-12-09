names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']
for name in names:
    print(name.title())


def list_sum(input_list):
    sum = 0
    for item in input_list:
        sum += int(item)
    return sum


test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))
