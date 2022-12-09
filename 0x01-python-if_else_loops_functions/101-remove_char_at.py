#!/usr/bin/python3
def remove_char_at(str, n):
    for char in str:
        if(char != n):
            print(f"{char}", end='')
