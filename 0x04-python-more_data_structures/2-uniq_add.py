#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set(my_list)
    result = 0
    for integer in unique_integers:
        result += integer
    return result
