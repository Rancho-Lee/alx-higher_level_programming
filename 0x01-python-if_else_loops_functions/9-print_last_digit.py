#!/usr/bin/python3
def print_last_digit(number):
    if(number < 0):
        Last_digit_number = (number % -10) * -1
    else:
        Last_digit_number = number % 10
    print(Last_digit_number, end='')
    return Last_digit_number
