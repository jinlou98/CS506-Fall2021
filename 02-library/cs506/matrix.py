# importing Numpy package
import numpy as np
from functools import reduce

# Takes in a matrix (list of lists) 
# and returns the determinant of the matrix.
def get_determinant(n_array):  
    # calculating the determinant of matrix
    # det = np.linalg.det(n_array)
    # return det

    order=len(n_array)
    det_positive = 0
    det_negative = 0

    for i in range(order):
        det_positive += reduce((lambda x, y: x * y), [n_array[(i+j)%order][j] for j in range(order)])

    for i in range(order):
        det_negative += reduce((lambda x, y: x * y), [n_array[(order-i-j)%order][j] for j in range(order)])
    
    det = det_positive - det_negative
    return det

# local testing
# creating a 2X2 Numpy matrix

# n_array = np.array([[10, 20, 4], [10, -20, 30], [6, 20, 9]])
# det = get_determinant(n_array)

# Displaying the Matrix

# print("Numpy Matrix is:")
# print(n_array)
# print("Determinant of given 2X2 matrix:")
# print(int(det))