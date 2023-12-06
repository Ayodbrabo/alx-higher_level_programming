#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set()
    for num in my_list:
        unique_list.add(num)
    result = sum(unique_list)
    return result
