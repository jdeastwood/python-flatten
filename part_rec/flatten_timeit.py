"""Wrapper code to test flatten functions.
"""
from compiler.ast import flatten
import random
import sys
import timeit

from my_flatten import my_flatten

random.seed("listoflists")

N_ITEMS = 10 ** 2
TIMEIT_ITERATIONS = 10 ** 2

rand_digit = lambda: random.randint(0,9)
go_deeper = lambda: random.choice([True, False])


def rand_list(curr_depth, max_len=5, max_depth=5):
    list_ = []
    for _ in range(random.choice(range(max_len + 1))):
        if go_deeper() and curr_depth < max_depth:
            list_.append(rand_list(curr_depth + 1))
        else:
            list_.append(rand_digit())
    return list_


def rand_list_of_lists(n_items):
    list_of_lists = []
    for _ in range(n_items):
        list_of_lists.append(rand_list(0))
    return list_of_lists

if __name__ == "__main__":
    setup = """
from flatten_timeit import rand_list, rand_list_of_lists
from my_flatten import my_flatten

lol = rand_list_of_lists({0})
""".format(N_ITEMS)
    stmt = "my_flatten(lol)"

    # check my_flatten first
    lol = rand_list_of_lists(N_ITEMS)
    assert flatten(lol) == my_flatten(lol), "Your my_flatten did not flatten the list of lists properly."

    # time my_flatten second
    sys.stdout.write("Your my_flatten function took: {0} seconds to run {1} times.\n".format(
        timeit.timeit(stmt, setup=setup, number=TIMEIT_ITERATIONS), TIMEIT_ITERATIONS))
