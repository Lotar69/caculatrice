def ask_user(sentence = "Saisir un chiffre"):
    choice = input(f"""{sentence}\n>""")
    return choice

def addition(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
            number = ask_user("Saisir un chiffre à additionner ou clicker sur '=' ")
    result = sum(list_numbers)
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit:
        if number.isdigit():
            number = int(number)
            list_numbers.append(number)
            number = ask_user("Saisir un chiffre à soustraire ou clicker sur '=' ")
            i = 0
            for list_number in list_numbers:
                if i == 0:
                    result = list_number
                    i += 1
                else:
                    result = result - list_number
        else:
            break
    return result

def multiplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            number = int(number)
            list_numbers.append(number)
        number = ask_user("Saisir un chiffre à multiplier ou clicker sur '=' ")
        i = 0
        for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
            if i == 0:
                result = list_number
                i += 1
            else:
                result = result * list_number
    return result

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            number = int(number)
            list_numbers.append(number)
        number = ask_user("Saisir un chiffre à diviser ou clicker sur '=' ")
        i = 0
        for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
            if i == 0:
                result = list_number
                i += 1
        else:
            result = result / list_number
            result = int(result)
    return result

def display_interface():
    choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
    while choice.isdigit():
        choice = int(choice)
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            result = multiplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")
            result = division(choice)
        return print(f"Le resultat est ==> {result}")

display_interface()