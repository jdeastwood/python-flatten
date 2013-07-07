import pyximport; pyximport.install()
from my_flatten_c import my_flatten_cython

def my_flatten(list_of_lists):
    return my_flatten_cython(list_of_lists)
