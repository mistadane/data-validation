import string
import random


# get data from user
def user_details():
    first_name = input("Enter first Name: ")
    last_name = input("Enter Last name: ")
    user_email = input("Enter a valid email address: ")
    details = [first_name, last_name, user_email]

    return details


# Generate password using details
def gen_password(details):

    char = string.ascii_letters
    length = 5
    a = ''.join(random.choice(char) for i in range(length))

    password = str(details[0][0:2] + details[1][-2:] + a)
    return password


# main program
status = True
container = []

while status:
    # get user details
    details = user_details()

    # show password generated
    password = gen_password(details)
    print(f"Your password is: {password}")

    # ask user if he/she likes password
    password_answer = input('Do you want to keep this password (Y)Yes or (N)No: ')

    password_loop = True

    while password_loop:

        if password_answer.upper() == 'Y':
            details.append(password)
            container.append(details)

            password_loop = False

        else:
            # ask user to enter preferred password
            password_choice = input('Enter preferred password: ')

            # Password len loop
            pass_len = True

            while pass_len:
                if len(password_choice) >= 7:
                    details.append(password_choice)
                    container.append(details)

                    pass_len = False

                    password_loop = False

                else:
                    print('You entered password less than 7 characters')
                    password_choice = input('Enter a password equal or more than 7 characters: ')

    new = input('Enter new user (Y)Yes or (N)No: ')
    if new.upper() == 'N':
        status = False
        for item in container:
            print(item)

    else:
        status = True








