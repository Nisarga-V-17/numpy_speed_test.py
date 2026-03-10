import time
import numpy as np

# Create 1 million numbers using Python list
python_list = list(range(1000000))

# Create 1 million numbers using NumPy
numpy_array = np.arange(1000000)

# Test Python list operation
start_time = time.time()

squared_list = [x**2 for x in python_list]

end_time = time.time()
python_time = end_time - start_time

# Test NumPy array operation
start_time = time.time()

squared_array = numpy_array ** 2

end_time = time.time()
numpy_time = end_time - start_time

print("Python List Execution Time:", python_time)
print("NumPy Array Execution Time:", numpy_time)