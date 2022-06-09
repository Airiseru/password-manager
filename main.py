"""
This program is a password manager that will store a user's password. It will also create a new password if stated. It is terminal based.

Usage (in Linux):
python3 main.py new <keyword> - Generates a new random password for keyword
python3 main.py list - Displays all the keywords with passwords
python3 main.py del <keyword> - Deletes the password and keyword
python3 main.py <keyword> - Pastes the password into the clipboard
"""

# imports
# from pathlib import Path
import pyperclip
import sys
import random
import shelve

# function to generate random password
def random_pass():
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    special_char = '!#$&.?'
    numbers = '0123456789'

    options_pass = list(uppercase_letters + lowercase_letters + special_char + numbers + numbers + special_char)
        # added numbers and special_char twice so that it's more random

    random.shuffle(options_pass)
    final_pass = ''

    for i in range(12):
        final_pass += random.choice(options_pass)

    return final_pass

if __name__ == '__main__':
    # create data file
    pass_file = shelve.open('pass-data')

    # check arguments entered when running main.py
    if len(sys.argv) < 2:
        print("Check README.md for proper usage of program.")

    elif len(sys.argv) == 3:
        # generate new password saved in a specific keyword
        if sys.argv[1].lower() == 'new':
            password = random_pass()
            pass_file[sys.argv[2]] = password
            print("Password for " + sys.argv[2] + " has been generated")

        # deletes a certain keyword and password
        elif sys.argv[1].lower() == 'del':
            try:
                del pass_file[sys.argv[2]]
                print("Password for " + sys.argv[2] + " has been deleted")
            except:
                print("Error has occured. Please check the spelling of keyword.")

    # display all keywords saved
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(pass_file.keys())))
        print("The keywords available is in your clipboard.")

    # places password into the clipboard
    elif len(sys.argv) == 2:
        keyword = sys.argv[1]
        if keyword in pass_file.keys():
            pyperclip.copy(pass_file[keyword])
            print("The password for " + keyword + " is in your clipboard.")
        else:
            print(keyword + " and its password does not exist.")


    pass_file.close()
