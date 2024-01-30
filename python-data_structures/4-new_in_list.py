#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_my_list = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return copy_my_list[element]

    copy_my_list[idx] = element
    return copy_my_list
