# Password Manager and Creator

This program uses different modules to generate a random password, saves the password, and access the password (by putting it in the user's clipboard for them to paste it)

This program is similar to the class-link-clipboard program (https://github.com/Airiseru/class-link-clipboard). It uses similar modules so download instructions will be there.

## Usage
`python main.py new <keyword>`
- Generates a new password for keyword
    - keyword can be name of website or app (e.g. facebook, twitter, wikipedia)

`python main.py list`
- Displays all the keyword available in the data file

`python main.py <keyword>`
- Get the password for keyword. The password will be "pasted" into the clipboard for easy pasting

`python main.py del <keyword>`
- Delete the password for keyword from the data file
