# Name : Yogi Halagunaki
# Assignment No: 3(Que2)

# Questions 2:
# Accept two lists of 5 elements each from the user.
# Convert them to numpy arrays. Concatenate these arrays and print it. Also sort these arrays and print it.

import numpy as np

my_list_one = []
my_list_two = []

for i in range(5):
    my_input = int(input())
    my_list_one.append(my_input)

print("List one :",my_list_one)

for i in range(5):
    my_input = int(input())
    my_list_two.append(my_input)

print("List Two", my_list_two)

# conversion of List to Array

my_array_one = np.array(my_list_one)
my_array_two = np.array(my_list_two)
print("List to array convert 1 :", my_array_one)
print("List to array convert 2 :", my_array_two)

# concatenation of arrays

array_concat = np.concatenate((my_array_one, my_array_two))

print("concatenation of arrays are :", array_concat)

# Sorting of array

print("Sorted array :", np.sort(array_concat))


#
# Output :
# 1
# 5
# 8
# 9
# 6
# List one : [1, 5, 8, 9, 6]
# 2
# 4
# 8
# 7
# 6
# List Two [2, 4, 8, 7, 6]
# List to array convert 1 : [1 5 8 9 6]
# List to array convert 2 : [2 4 8 7 6]
# concatenation of arrays are : [1 5 8 9 6 2 4 8 7 6]
# Sorted array : [1 2 4 5 6 6 7 8 8 9]

# Process finished with exit code 0
