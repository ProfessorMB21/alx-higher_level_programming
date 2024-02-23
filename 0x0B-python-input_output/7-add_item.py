#!/usr/bin/python
"""
A script that adds all supplied arguments to a Python list
and then save it as a JSON representation to a file
"""
import sys

if __name__ = "__main__":
    save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file.py').load_from_json_file

    try:
        args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args = []

    args.extend(sys.argv[1:])
    save_to_json_file(args, "add_item.json")


