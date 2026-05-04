from  random import choice
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the PyPassword Generator!")
numbers_letters = int(input("How many letters would you like in your password?\n"))
numbers_symbols = int(input(f"How many symbols would you like?\n"))
numbers_numbers = int(input(f"How many numbers would you like?\n"))

def password(numbers_letters, numbers_symbols, numbers_numbers):

 

    password = []
    for digital in range(0, numbers_letters):
        password.append(choice(letters))

    for digital in range(0, numbers_symbols):
        password.append(choice(symbols))

    for digital in range(0, numbers_numbers):
        password.append(choice(numbers))



    shuffle(password)
    safe_password = ''
    for iten in password:
        safe_password += iten
    return f"Here is your password: {safe_password}"


password(numbers_letters, numbers_symbols, numbers_numbers)
