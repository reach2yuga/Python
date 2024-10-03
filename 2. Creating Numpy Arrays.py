#Creating Numpy Arrays

'''Summary:
=> You can create arrays from Python lists/tuples.
=> NumPy provides functions like zeros(), ones(), arange(), linspace(), and random() 
   to generate arrays with specific values.
'''
print("------------------------------------------------------")
# 1] From a Python List or Tuple:
import numpy as np

# A] From a list
arr1 = np.array([1, 2, 3, 4, 5])

# B] From a tuple
arr2 = np.array((6, 7, 8, 9, 10))

print("From a list => ",arr1)
print("From a tuple => ",arr2)

print("------------------------------------------------------")

# 2] Using Built-in NumPy Functions:#

# a] . np.zeros(shape): Creates an array filled with zeros. 
arr3 = np.zeros((3, 4))  # 3x4 array of zeros
print("Creates an array filled with zeros => \n", arr3)
 
 # b] np.ones(shape): Creates an array filled with ones.
arr4 = np.ones((2, 3))  # 2x3 array of ones
print("Creates an array filled with ones => \n", arr4)

# c] np.full(shape, fill_value): Creates an array filled with a specified value.
arr5 = np.full((2, 2), 7)  # 2x2 array filled with 7
print("Creates an array filled with a specified value\n" ,arr5)

# d] np.eye(N): Creates an identity matrix (N x N matrix with ones on the diagonal and zeros elsewhere)
arr6 = np.eye(3)  # 3x3 identity matrix
print("matrix with ones on the diagonal and zeros elsewhere\n",arr6)

# e] np.arange(start, stop, step): Creates an array with values ranging from start to stop
# with a specific step size.
arr7 = np.arange(0, 10, 2)  # Array of even numbers from 0 to 8
print("Creates an array with values ranging from start to stop with a specific step size\n",arr7)

# f] np.linspace(start, stop, num): Creates an array with num evenly spaced values between start and stop.
arr8 = np.linspace(0, 1, 5)  # 5 evenly spaced numbers between 0 and 1
print("Creates an array with num evenly spaced values between start and stop\n",arr8)

# g] np.random.rand(shape): Creates an array with random values between 0 and 1.
arr9 = np.random.rand(3, 3)  # 3x3 array of random values
print("Creates an array with random values between 0 and 1\n",arr9)







