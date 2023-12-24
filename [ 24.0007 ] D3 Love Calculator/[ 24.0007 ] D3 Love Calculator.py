# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_math_TRUE = 0
total_math_LOVE = 0

combined_total_math = 0

combined_names = name1 + name2
# print(combined_names)

combined_lower_names = combined_names.lower()
# print(combined_lower_names)

T = 0
R = 0
U = 0
E1 = 0

L = 0
O = 0
V = 0
E2 = 0

T = (combined_lower_names.count("t"))
if T > 0:
    total_math_TRUE += T
    # print(f"T = {T}")
    # print(f"Total score so far is {total_math_TRUE} ")

R = (combined_lower_names.count("r"))
if R > 0:
    total_math_TRUE += R
    # print(f"R = {R}")
    # print(f"Total score so far is {total_math_TRUE} ")

U = (combined_lower_names.count("u"))
if U > 0:
    total_math_TRUE += U
    # print(f"U = {U}")
    # print(f"Total score so far is {total_math_TRUE} ")

E1 = (combined_lower_names.count("e"))
if E1 > 0:
    total_math_TRUE += E1
    # print(f"E = {E1}")
    # print(f"Total score so far is {total_math_TRUE} ")


L = (combined_lower_names.count("l"))
if L > 0:
    total_math_LOVE += L
    # print(f"L = {L}")
    # print(f"Total score so far is {total_math_TRUE} ")

O = (combined_lower_names.count("o"))
if O > 0:
    total_math_LOVE += O
    # print(f"O = {O}")
    # print(f"Total score so far is {total_math_TRUE} ")

V = (combined_lower_names.count("v"))
if V > 0:
    total_math_LOVE += V
    # print(f"V = {V}")
    # print(f"Total score so far is {total_math_TRUE} ")

E2 = (combined_lower_names.count("e"))
if E2 > 0:
    total_math_LOVE += E2
    # print(f"E = {E2}")
    # print(f"Total score so far is {total_math_TRUE} ")


#below: you must concatenate the total of TRUE and the total of LOVE as 2
#numbers side-by-side to each other, so the total (in integers) must be converted
#into strings, HOWEVER, in order to do math with it in the following line,
#then after the string conversion, you also add a layer on interger conversion afterwards!
total_score = int(str(total_math_TRUE)+str(total_math_LOVE))
# print(total_score)

if total_score < 10 or total_score > 90:
    print("Your score is " + str(total_score) + ", you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print("Your score is " + str(total_score) + ", you are alright together.")
else:
    print("Your score is " + str(total_score) + ".")

'''
For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
'''