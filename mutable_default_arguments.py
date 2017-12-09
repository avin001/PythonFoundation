# Default arguments are a helpful feature, but there is one situation where they can be surprisingly unhelpful. Using a mutable type (like a list or dictionary) as a default argument and then modifying that argument can lead to strange results. It's usually best to avoid using mutable default arguments.


def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list


# The list object base_list is only created once: when the todo_list function is defined. Lists are mutable objects. This list object is used every time the function is called, it isn't redefined each time the function is called. Because todo_list appends an item to the list, base_list can get longer each time that todo_list is called.


print(todo_list('check the mail'))
print(todo_list('begin orbital transfer'))
