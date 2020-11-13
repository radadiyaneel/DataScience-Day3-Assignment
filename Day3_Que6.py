# Name : Yogi Halagunaki
# Assignment No: 3(Que 6)

# Questions 6:
# How to get unique items and counts of unique items?


import numpy as np

arr = np.array([4, 7, 8, 9, 5, 6, 5, 4, 4])

unique, counts = np.unique(arr, return_counts=True)
arr = np.asarray((unique, counts)).T
print(arr)

# Output : /home/yogi/Desktop/Python_Code/venv/bin/python
# /home/yogi/Desktop/Python_Code/Lets_Upgrade_Assignments/Day3/Day3_Que6.py

# [[4 3]
#  [5 2]
#  [6 1]
#  [7 1]
#  [8 1]
#  [9 1]]

# Process finished with exit code 0
