# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):  # For Loop #1, for heights
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

counter = 0  # this replicates the len() function
total_height_so_far = 0

# (key component, it’s “each_student, not “student_heights” that you get the height from to add to the total!)

for each_student in student_heights:  # For Loop #2, for the quantity of students
    print(f"Iteration # {counter}")
    print(f"This individual student's height, this round, is: {each_student}")
    print(f"The counter is at: {counter}")
    counter += 1
    total_height_so_far += each_student  # this replicates the sum() function
    print(f"The total height so far this round is: {total_height_so_far}")
    x = (total_height_so_far / counter)
    print(f"The average height so far is: {x}")
    print()

print(f"The final height total is {total_height_so_far} ")
x = (total_height_so_far / counter)
print(f"The average height is: {x}")
