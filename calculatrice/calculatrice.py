def ask_user(sentence = "Type a number:"): # change all the names of functons (function have to be lowercase
    choice = input(f"""{sentence}\n>""")
    return choice

def add(): # do_something
    """Functions to add numbers"""
    res = 0
    number = ask_user("Type a number to add or type = to get the result:")
    while number.isdigit():
        res += int(number)
        number = ask_user("Type a number to add or type = to get the result:")
    return res

def multiply():
    """Functions to multiply numbers"""
    res = 1
    number = ask_user("Type a number to multiply or type = to get the result:")
    while number.isdigit():
        res *= int(number)
        number = ask_user("Type a number to multiply or type = to get the result:")
    return res

def divide():
    """Functions to divide numbers"""
    res = 0 # result if no number were typed
    first_number = ask_user("Type a number to divide or type = to get the result:")
    if first_number.isdigit():
        res = int(first_number)
        number = ask_user("Type a number to divide or type = to get the result:")
        while number.isdigit():
            # here we need to catch an error
            if int(number) == 0 :
                return 0
            res /= int(number)
            number = ask_user("Type a number to divide or type = to get the result:")
        else:
            res = res
    return res

def substract():
    """Functions to substract numbers"""
    res = 0
    number = ask_user("Type a number to substract or type = to get the result:")
    if number.isdigit():
        res = int(number)
    else:
        return res
    while number.isdigit: # do_something
        number = ask_user("Type a number to substract or type = to get the result:")
        if not number.isdigit():
            return res
        res -= int(number)
    return res

def display_interface():
    choice = ask_user("""
    Type :
    1 - to add numbers
    2 - to substract numbers
    3 - to multiply numbers
    4 - to divide numbers""")
    while choice.isdigit():
        if choice == '1':
            result = add()
        elif choice == '2':
            result = substract()
        elif choice == '3':
            result = multiply()
        elif choice == '4':
            result = divide()
        print(f"The result is ==> {result}")
        break #exit while cycle after showing the result of calculation





