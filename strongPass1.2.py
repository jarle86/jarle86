import getpass

def validate_length(user_password):
    return len(user_password) >= 8

def validate_upper(user_password):
    return any(char.isupper() for char in user_password)

def validate_lower(user_password):
    return any(char.islower() for char in user_password)

def validate_char_or_number(user_password, char_list):
    return any(char in char_list for char in user_password)

def get_rate():
    rate = 0
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', ',', '<', '>', '.', '?', '/']

    rate += validate_length(user_password)
    rate += validate_upper(user_password)
    rate += validate_lower(user_password)
    rate += validate_char_or_number(user_password, char_list)
    rate += validate_char_or_number(user_password, num_list)

    return print(f'Your password rate: {rate}/5.')

user_password = getpass.getpass("Please type your credential to be evaluated: ")
get_rate()
