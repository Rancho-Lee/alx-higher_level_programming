#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a[1] = 0
    if len(tuple_b) < 2:
        tuple_b[1] = 0
    i = 0
    while i < 2:
        new_tuple = tuple_a[i] + tuple_b[i]
        i += 1
    print("{:d}".format(new_tuple), end=', ')
