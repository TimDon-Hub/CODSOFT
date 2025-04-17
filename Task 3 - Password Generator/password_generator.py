'''
CODSOFT TASK 3

PASSWORD GENERATOR
    A password generator is a useful tool that generates strong and
    random passwords for users. This project aims to create a
    password generator application using Python, allowing users to
    specify the length and complexity of the password.
    User Input: Prompt the user to specify the desired length of the
    password.
    Generate Password: Use a combination of random characters to
    generate a password of the specified length.
    Display the Password: Print the generated password on the screen.
'''

import string
import random

def generate_password(min_length, complexity):
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    all_characters = letters + numbers + special_characters

    password = ''
    for i in range(min_length):
        if complexity == 'l':
            char = random.choice(letters)
            password += char
        elif complexity == 'm':
            char = random.choice(letters + numbers)
            password += char
        elif complexity == 'h':
            char = random.choice(all_characters)
            password += char

    return password


min_length = int(input('Enter length of password: '))
complexity = input('Select complexity of password; LOW(l) - MEDIUM(m) - HIGH(h): ').lower()
print(f'Password generated: {generate_password(min_length, complexity)}')