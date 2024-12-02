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
    # Check if all decreasing
    if np.all(dx <= 0):
        return np.all((np.abs(dx) >= lower_bound) & (np.abs(dx) <= upper_bound))
    elif np.all(dx >= 0):
        return np.all((dx >= lower_bound) & (dx <= upper_bound))
    else:
        return False

def main():
    list_lines = parse(FILE_NAME)
    count = 0
    for line in list_lines:
        if monotonic(line):
            count += 1
    print(count)

if __name__ == "__main__":
    main()