# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#input data: 78 65 89 86 55 91 64 89

iteration_counter = 0

for score in student_scores:
    # print(score)
    iteration_counter += 1
            # print(score[len(student_scores)])
    # print(iteration_counter)
    # print(len(student_scores))

sorted_scores = sorted(student_scores)       #(replicates the max( ) function)
# print(f"Sorted scores, in order, is: {sorted_scores}")
updated_sorted_scores = sorted_scores[-1]
print(f"The highest score in the class is: {updated_sorted_scores}")