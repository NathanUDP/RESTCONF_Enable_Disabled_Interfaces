import string


def input_validation(user_input):
    while True:
        if user_input.lower() == 'y' or user_input.lower() == 'n':
            return user_input
            break
        else:
            print("That input is not valid, please try again")
            user_input = input(">")

def input_validation_count(interface_en_count, list_count):
    while not interface_en_count.isdigit():
        print("Value most be numeric. Please try again")
        interface_en_count = input(">")
    while True:
        if int(interface_en_count) <= list_count:
            return interface_en_count
        else:
            print("-" * 25)
            print("That is too many interfaces. Please try again")
            interface_en_count = input(">")

def enabled_interface_list(interface_en_count, disable_interface_list):
    interface_en_count = int(interface_en_count)
    enabled_list = []
    i = 1
    while interface_en_count > 0:
        print("-" * 25)
        print(f"Please enter the {i} interface you would like enabled")
        cur_interface = input(">")
        while not cur_interface.strip() in disable_interface_list:
           print('!' * 15)
           print("That interface does not exist or is already enabled. Please try again.")
           cur_interface = input(">")
        enabled_list.append(cur_interface)
        i += 1
        interface_en_count -= 1
    return enabled_list
