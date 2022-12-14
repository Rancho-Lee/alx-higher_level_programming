#!/usr/bin/python3
def element_at(my_list, idx):
    lent = len(my_list) - 1
    if idx < 0 or idx > lent:
        return None
