#Password Generator Project (Easy-mode)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


quantity_of_letters = int(input("How many letters would you like in your password? "))
quantity_of_numbers = int(input("How many numbers would you like in your password? "))
quantity_of_symbols = int(input("How many symbols would you like in your password? "))


current_password = ""

for letter in range(0, quantity_of_letters):
    l = random.choice(letters)
    current_password += str(l)

for number in range(0, quantity_of_numbers):
    n = random.choice(numbers)
    current_password += str(n)

for symbol in range(0, quantity_of_symbols):
    s = random.choice(symbols)
    current_password += str(s)

print(f"Your password will be: {current_password}")


'''
Basically looping this below:

l = random.choice(letters)
print(l)

n = random.choice(numbers)
print(n)

s = random.choice(symbols)
print(s)

current_password = current_password+l+n+s
print(f"Your password is currently {current_password}")
'''