def ask_user(sentence = "Saisir un chiffre"):   #CamelCase removed.
    choice = input(f"""{sentence}\n>""")
    return choice

def addition(number):   #Uppercase removed
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
            number = ask_user("Saisir un chiffre à additionner ou clicker sur '=' ")
    result = sum(list_numbers)  #List summarized
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit:
        if number.isdigit():
            number = int(number)    #Number transformed into integer
            list_numbers.append(number)
            number = ask_user("Saisir un chiffre à soustraire ou clicker sur '=' ")
            i = 0
            for list_number in list_numbers:
                if i == 0:
                    result = list_number
                    i += 1
                else:
                    result = result - list_number
        else:   #Add a break to the loop
            break
    return result

def multiplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            number = int(number)    #Number transformed into integer
            list_numbers.append(number)
        number = ask_user("Saisir un chiffre à multiplier ou clicker sur '=' ")
        i = 0
        for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
            if i == 0:      #0 changed from string to a number
                result = list_number
                i += 1
            else:
                result = result * list_number   #Changed the operator from a (divide) / to a (multiply)*
    return result

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            number = int(number)    #Number transformed into integer
            list_numbers.append(number)
        number = ask_user("Saisir un chiffre à diviser ou clicker sur '=' ")
        i = 0
        for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
            if i == 0:
                result = list_number
                i += 1
        else:
            result = result / list_number   #Changed the operator from a (plus) + to a (divide) /
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
        choice = int(choice)    #choice transformed into integer
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
        else:
            print("Mauvaise réponse")
            print("----------------")
            display_interface()
        return print(f"Le resultat est ==> {result}")

display_interface()