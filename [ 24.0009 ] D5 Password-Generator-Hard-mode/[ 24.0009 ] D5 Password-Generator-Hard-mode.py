#Password Generator Project (Hard-mode: all characters completely randomized of their order)
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

print(f"Password before the shuffle is: {current_password}\n")

# Shuffling the entire password around:

# Convert the word to a list of characters
converting_word_to_list_of_chars = list(current_password)

password_list = list(current_password)

# Shuffle the list of characters
random.shuffle(password_list)

# Join the list back into a string
shuffled_word = ''.join(password_list)

print(f"Your final generated password will be {shuffled_word}")


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
