# Name : Yogi Halagunaki
# Assignments No: 3(Que 4)

# Questions 4:
# How to convert a 1D array into a 2D array? Demonstrate with the help of a code snippet
# Hint: np.newaxis, np.expand_dims

import numpy as np

arr = np.arange(int(input()))
print("Test 1D array (shape) :", arr.shape)

two_d_array_row = arr[np.newaxis]
print("Test` 2D array for row is :", two_d_array_row.shape)

two_d_array_col = arr[:, np.newaxis]
print("Test` 2D array for column is :", two_d_array_col.shape)
# Output :
# 10
# Test 1D array (shape) : (10,)
# Test` 2D array for row is : (1, 10)
# Test` 2D array for column is : (10, 1)
# 
# Process finished with exit code 0
