def my_flatten(list_of_lists):
    l = []
    for elem in list_of_lists:
        t = type(elem)
        if t is tuple or t is list:
            for elem2 in my_flatten(elem):
                l.append(elem2)
        else:
            l.append(elem)
    return l
