#!/usr/bin/python3
def no_c(my_string):
    while (my_string.count('c')):
        my_string.remove('c')
    while (my_string.count('C')):
        my_string.remove('C')
    return my_string
