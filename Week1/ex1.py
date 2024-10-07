# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

# Answer:
positive_count = negative_count = 0
for item in data1:
    if item > 0:
        positive_count +=1
    if item < 0:
        negative_count +=1
print("The number of positive numbers in the list is: ", positive_count)
print("The number of negative numbers in the list is: ", negative_count)