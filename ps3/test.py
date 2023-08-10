import numpy as np

# Creating two example arrays
array1 = np.random.rand(200,1,3)
array2 = np.random.rand(16,3)

# Broadcasting and performing element-wise operation (e.g., addition)
result = np.argmin(np.linalg.norm(array1 - array2, axis = 2), axis = 1)

# The result will have the shape (200, 3), and each element will be the sum of the corresponding elements from array1 and array2.
print(result.shape)  # Output: (200, 3)