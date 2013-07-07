def my_flatten(list_of_lists, accumulator=[]):
    for elem in list_of_lists:
        t = type(elem)
        if t is list or t is tuple:
            my_flatten(elem, accumulator)
        else:
            accumulator.append(elem)
    return accumulator
