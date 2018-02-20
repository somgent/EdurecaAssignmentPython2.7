
#====Create random vector of size 50 and replace the maximum value by 0 and minimum value by 100.====

import numpy as np

rand_vector = np.random.randint(low=1, high=100, size=50)
print '\n',rand_vector,'\n'
print "-" * 12 + "Replacing the min value with 0 and max value with 100" + "-" * 12

# Sorting the array. array[0] will have the min value and array[len-1] will have max value.
rand_vector.sort()
min_val = rand_vector[0]
max_val = rand_vector[49]
print "\t\t\tMinimum Value Elemnet=", min_val, "\tMaximum Value Element=", max_val,'\n'

for index, val in enumerate(rand_vector):
    if val == min_val:
        rand_vector[index] = 0
    elif val == max_val:
        rand_vector[index] = 100

print rand_vector