# encoding: utf-8
# cython: profile=True
# filename: calc_pi.py

cimport cpython

DEF MAX_DEPTH = 10

cdef struct stack_frame:
    int idx
    int lnth
    cpython.PyObject *lst

def my_flatten_cython(list_of_lists):
    cdef list accumulator = []
    cdef stack_frame stack[MAX_DEPTH + 1]
    cdef int stack_ptr = 0
    cdef int idx = 0
    cdef int length = 0
    cdef list list_ptr
    cdef type t

    stack[0].lst = <cpython.PyObject *>list_of_lists
    stack[0].idx = 0
    stack[0].lnth = len(list_of_lists)

    while stack_ptr > -1:
        list_ptr = <list> stack[stack_ptr].lst
        idx = stack[stack_ptr].idx
        length = stack[stack_ptr].lnth
        stack_ptr -= 1

        while idx < length:
            elem = list_ptr[idx]
            t = type(elem)
            if t is list or t is tuple:
                stack_ptr += 1
                stack[stack_ptr].lst = <cpython.PyObject *>list_ptr
                stack[stack_ptr].idx = idx + 1
                stack[stack_ptr].lnth = length
                idx, list_ptr = 0, elem
                length = len(elem)
            else:
                accumulator.append(elem)
                idx += 1
    return accumulator

