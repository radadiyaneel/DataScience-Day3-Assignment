# Name : Yogi Halagunaki
# Assignment NO : 3(Que 5)

# Questions 5:
# Consider two square numpy arrays. Stack them vertically and horizontally.
# Hint: Use vstack(), hstack()

import numpy as np

my_array_one = np.square([1, 4, 5, 8, 79, 6, 3, 5, 7, 5, 9, 6, 4, 5])  # square of numpy array
my_array_two = np.square([4, 5, 8, 6, 9, 7, 4, 5, 6])  # square of numpy array


print(" horizontally stacked :", np.hstack((my_array_one, my_array_two)))

print("vertically stacked : ", np.hstack((my_array_one, my_array_two)))


# Output :
#  horizontally stacked : [   1   16   25   64 6241   36    9   25   49   25   81   36   16   25
#    16   25   64   36   81   49   16   25   36]
# vertically stacked :  [   1   16   25   64 6241   36    9   25   49   25   81   36   16   25
#    16   25   64   36   81   49   16   25   36]

# Process finished with exit code 0
