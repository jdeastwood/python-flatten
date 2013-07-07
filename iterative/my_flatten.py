def my_flatten(list_of_lists):
    accumulator = []
    stack = [(0,list_of_lists)]

    while stack:
        idx, list_ptr = stack.pop()
        while idx < len(list_ptr):
            elem = list_ptr[idx]
            t = type(elem)
            if t is list or t is tuple:
                stack.append((idx + 1, list_ptr))
                idx, list_ptr = 0, elem
            else:
                accumulator.append(elem)
                idx += 1
    return accumulator

