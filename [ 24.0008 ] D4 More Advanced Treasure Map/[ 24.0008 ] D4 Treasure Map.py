# 🚨 Don't change the code below 👇
row1 = ["⬜️️","⬜️️","⬜️️"]
row2 = ["⬜️️","⬜️️","⬜️️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

x_axis_horizontal = int(position[0]) #position is a string, convert to int
y_axis_vertical = int(position[1]) #get each x and y axis as individual integers

'''
selected_row = map[y_axis_vertical-1] #start the search with the vertical scan (y-axis)
selected_row[x_axis_horizontal-1] = "X"
'''

#OR

#Alt efficient code:

map[y_axis_vertical-1][x_axis_horizontal-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#YES, YOU HAVE TO REPRINT OUT THE BOARD. You weren't doing that before!!! :O