#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == my_list:
            new_list.append(search)
        else:
            new_list.append(i)
            return new_list

