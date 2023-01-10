#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
lst = []

for items in sys.argv[1:]:
    lst.append(items)
    load_from_json_file(file_name)

save_to_json_file(lst, file_name)
