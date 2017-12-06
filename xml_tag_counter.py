def tag_count(input_list):
    count = 0
    for item in input_list:
        if str(item).startswith("<") and str(item).endswith(">"):
            count += 1
    return count


list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
