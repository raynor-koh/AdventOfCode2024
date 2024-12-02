# NOTE: The data is of varying lengths therefore numpy cannot be used directly.
import numpy as np
from typing import List

FILE_NAME = "input.txt"
# Function to pass the input.txt
def parse(file_name: str) -> List[List[int]]:
    output = None
    with open(file=file_name, mode="r") as file:
        all_lines = file.readlines()
        
        # Function to convert a list of strings to a list of integers
        def mapping_function(xs: List[str]) -> List[int]:
            xs = xs.strip().split(" ")
            return np.array(list(map(int, xs)))

        output = list(map(mapping_function, all_lines))
    return output

# Function to check if monotonically decreasing or increasing
def monotonic(x: np.ndarray) -> bool:
    lower_bound = 1
    upper_bound = 3
    dx = np.diff(x)

    # Function to check if the differences are within range
    def within_range(x: np.ndarray):
        return np.all((np.abs(dx) >= lower_bound) & (np.abs(dx) <= upper_bound))
    # Check if all decreasing
    if np.all(dx <= 0) and within_range(dx):
        return True
    elif np.all(dx >= 0) and within_range(dx):
        return True
    else:
        return False

# Function to check if the removal of maximum one element makes it monotonic
def can_be_monotonic(x: np.ndarray) -> bool:
    if monotonic(x):
        return True
    # Remove first position and check if monotonic
    if monotonic(np.delete(x, 0)):
        return True
    # Iterate and find the first violation
    diff = np.diff(x)
    for i in range(1, len(x)):
        last_difference = diff[i-1]
        curr_difference = diff[i]

        if not (0 < abs(curr_difference) <= 3) or (last_difference != 0 and curr_difference / last_difference <= 0):
            remove_current = np.delete(x, i)
            remove_next = np.delete(x, i+1)
            return monotonic(remove_current) or monotonic(remove_next)
    return False


def main():
    list_lines = parse(FILE_NAME)
    count = 0
    for line in list_lines:
        if can_be_monotonic(line):
            count += 1
    print(count)

if __name__ == "__main__":
    main()