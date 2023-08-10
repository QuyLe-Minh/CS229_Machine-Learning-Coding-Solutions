import numpy as np
 
x = np.array([[0, 3, 4], [1, 2, 4], [3, 4, 5], [6,7,8]])
 
print("Shape of array:\n", np.shape(x))
 
print("Covariance matrix of x:\n", np.cov(x))