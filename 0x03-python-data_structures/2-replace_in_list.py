#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num = 0
    if num <= idx < len(my_list):
        my_list[idx] = element
    return my_list
