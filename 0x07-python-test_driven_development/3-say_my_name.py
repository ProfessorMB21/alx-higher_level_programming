#!/usr/bin/python3
""" Defines a function that says my name """

def say_my_name(first_name, last_name=""):
    """
    Prints the fullname of the usr

    Args:
        first_name (str): First name of the user
        last_name (str): Last name of the user

    Raises:
        TypeError: If either first_name or last_name is non-str
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))


