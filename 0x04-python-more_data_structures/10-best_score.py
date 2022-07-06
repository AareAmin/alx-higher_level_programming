#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if my_dict[key] > my_dict[max]:
                max = key
            return max
    return None
