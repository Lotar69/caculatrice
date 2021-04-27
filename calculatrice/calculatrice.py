def ask_user(sentence = "Type a number:"): # change all the names of functons (function have to be lowercase
    choice = input(f"""{sentence}\n>""")
    return choice

def add(a,b): # do_something
    """Functions to add numbers"""
    return a+b

def multiply(a,b):
    """Functions to multiply numbers"""
    return a*b

def divide(a,b):
    """Functions to divide numbers"""
    return a/b

def substract(a,b):
    """Functions to substract numbers"""
    return a-b

def display_interface():
    choice = ask_user("""
    Type :
    1 - to add numbers
    2 - to substract numbers
    3 - to multiply numbers
    4 - to divide numbers""")
    if choice not in ['1','2','3','4']:
        print("Unknown command")
        return

    a = ask_user("Type first number:")
    if not a.isdigit():
        print(f"You did't type any number to make calculation" )
        return
    a = int(a)
    res = a
    b = ask_user("Type number or = to get the result:")
    if not b.isdigit():
        print(f"Your result is {res}" )
        return
    while b.isdigit():
        b = int(b)
        if choice == '1':
            res = add(a,b)
        elif choice == '2':
            res = substract(a,b)
        elif choice == '3':
            res = multiply(a,b)
        elif choice == '4':
            try:
                res = divide(a,b)
            except ZeroDivisionError:
                print("You can not devide by zero")
                return

        a = res
        b = ask_user("Type number or = to get the result:")
    print(f"Your result is {res}" )
    return #exit while cycle after showing the result of calculation





