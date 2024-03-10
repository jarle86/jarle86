import getpass

rate = 0

def validate_leng(user_password):
    #validate length
    if len(user_password) >= 8:
        global rate
        rate +=1
        return True
    return False

def validate_upper(user_password):
    #validate if there is at lease one letter is upper case
    for a in user_password:
        if a.isupper():
            global rate
            rate +=1
            return True
        else:
            continue
    return False

def validate_number(user_password):
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    #validate if there is at lease containt a number
    for a in user_password:
        if str(a) in num_list:
            global rate
            rate +=1
            return True
        else:
            continue
    return False

def validate_char(user_password):
    char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', ',', '<', '>', '.', '?', '/'] #chars
    #validate if there is at lease containt a number
    for a in user_password:
        if a in char_list:
            global rate
            rate +=1
            return True
        else:
            continue
    return False

user_password = getpass.getpass("Please type your credential to be evaluated: ")

print(validate_upper(user_password))
print(validate_leng(user_password))
print(validate_number(user_password))
print(validate_char(user_password))
print(f'your password rate {rate}/4.')