#!/usr/bin/python3
def best_score(a_dictionary):
    result = 0
    max = ""
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > result:
                max = key
                max = value
        return max
    else:
        return none
