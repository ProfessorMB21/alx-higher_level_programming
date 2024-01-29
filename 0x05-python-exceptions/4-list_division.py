#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ Divides element by element 2 lists """

    new = []
    for i in range(list_length):
        try:
            result = float(my_list_1[i]) / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        except (ValueError, TypeError):
            result = 0
            print("wrong type")
        finally:
            new.append(result)
    return result

