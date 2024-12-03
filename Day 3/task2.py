from typing import List
import re

VALID_PATTERN = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'

# Function to parse the corrupted input
def parse_corrupted(file_name: str) -> List[str]:
    output = []
    with open(file=file_name, mode="r") as file:
        all_lines = file.readlines()
        for line in all_lines:
            # Remove all invalid sequences
            matches = re.findall(VALID_PATTERN, line)
            output.extend(matches)
        return output

def compute_product(xs: List[str]) -> int:
    sum = 0
    flag = True
    for string in xs:
        if string == "don't()":
            flag = False
            continue
        elif string == "do()":
            flag = True
            continue
        elif flag:
            split = string.strip().split(",")
            first_number = int(split[0][4:])
            second_number = int(split[1][:-1])
            product = first_number * second_number
            sum += product
    print(f"Sum: {sum}")

def main():
    parsed_content = parse_corrupted("input.txt")
    compute_product(parsed_content)


if __name__ == "__main__":
    main()