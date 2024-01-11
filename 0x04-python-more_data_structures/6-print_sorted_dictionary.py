#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for v in sorted(a_dictionary.keys()):
        print("{}: {}".format(v, a_dictionary.get(v)))
