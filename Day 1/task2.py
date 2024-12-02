from typing import List
import numpy as np
# Create two lists to store the left and right inputs
left_list: List[int] = []
right_list: List[int] = []
with open("input.txt", mode="r") as file:
    all_lines = file.readlines()
    for line in all_lines:
        split = line.strip().split("   ")
        left, right = split[0], split[1]
        left_list.append(int(left))
        right_list.append(int(right))

# Convert List[int] into a numpy array of integers
left_list: np.ndarray = np.array(left_list, dtype=int)
right_list: np.ndarray = np.array(right_list, dtype=int)

# Create an array of counts
counts = np.array([np.sum(right_list== value) for value in left_list])

# Get the product
product = counts * left_list

# Compute sum
sum = np.sum(product)
print(sum)