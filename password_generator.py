def password_generator():
    """
    Returns a random password value containing alpha, numeric, and symbol characters

    Parameters:
    length (int): Desired length of password

    Output:
    password (str): New random password
    """

    # import modules
    import string
    import random


    # declare variables
    available_characters = ''
    password_list = []
    password = ''


    # ask for user parameters
    print("This program will allow you to create a complex new password. Please answer the following questions to begin.")
    print('')
    length = int(input("How many characters do you need in your password? Please limit your length to 50 characters or less. "))
    letters = input("Would you like to include letters in your password? (Y/N) ")
    numbers = input("How about numbers? (Y/N) ")
    symbols = input("Should we include special characters? (Y/N) ")


    # generate available characters
    if letters.upper() == 'Y':
        if numbers.upper() == 'Y':
            if symbols.upper() == 'Y':
                available_characters = string.ascii_letters + string.digits + string.punctuation
            elif symbols.upper() == 'N':
                available_characters = string.ascii_letters + string.digits
            else:
                available_characters = 'error'
        elif numbers.upper() == 'N':
            if symbols.upper() == 'Y':
                available_characters = string.ascii_letters + string.punctuation
            elif symbols.upper() == 'N':
                available_characters = string.ascii_letters
            else:
                available_characters = 'error'
    elif letters.upper() == 'N':
        if numbers.upper() == 'Y':
            if symbols.upper() == 'Y':
                available_characters = string.digits + string.punctuation
            elif symbols.upper() == 'N':
                available_characters = string.digits
            else:
                available_characters = 'error'
        elif numbers.upper() == 'N':
            if symbols.upper() == 'Y':
                available_characters = string.punctuation
            elif symbols.upper() == 'N':
                available_characters = 'no_values'
            else:
                available_characters = 'error'
        else:
            available_characters = 'error'
    else:
        available_characters = 'error'
    

    # identify potential errors with user-input length
    if isinstance(length, int) is False:
        length = 'error'
    elif length > 50:
        length = 'error'
    elif length < 1:
        length = 'error'


    # communicate error / processing messages
    if available_characters == 'error' or length == 'error':
        return "Looks like you didn't enter valid responses. Please try again."
    elif available_characters == 'no_values':
        return "Unable to generate a password. You must choose to include at least one of the following options: letters, numbers, or special characters."
    else:
        print("Thanks for the help!")
        print("Generating complex password now...")
        print("----------------------------------")


    # calculate password in list format
    password_list = random.sample(str(available_characters), length)


    # convert list to string output
    for x in password_list:
        password += x


    # return password
    return "Your new password: " + str(password)



print(password_generator())
