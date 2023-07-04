#!/usr/bin/python3
def magic_string():
    iteration = magic_string.iteration + 1 if hasattr(magic_string, 'iteration') else 1
    magic_string.iteration = iteration
    return "BestSchool" * iteration
