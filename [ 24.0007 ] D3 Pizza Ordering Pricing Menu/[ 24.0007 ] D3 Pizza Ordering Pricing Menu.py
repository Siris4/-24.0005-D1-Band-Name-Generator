# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_add_for_small = 2
pepperoni_add_for_medandlarge = 3
extra_cheese_price = 1

if size == "S":
    bill += small_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_add_for_small
elif size == "M":
    bill += medium_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_add_for_medandlarge
elif size == "L":
    bill += large_pizza_price
    if add_pepperoni == "Y":
        bill += pepperoni_add_for_medandlarge

if extra_cheese == "Y":
    bill += extra_cheese_price

print(f"Your final bill is ${bill}.")