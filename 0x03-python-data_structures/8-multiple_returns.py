#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = (0, "None")
    else:
        first_char = (len(sentence), sentence[0])
    return first_char
