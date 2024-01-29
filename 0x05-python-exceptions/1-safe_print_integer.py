#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with '{:d}'.format() """
    
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True

