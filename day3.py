## Day 3 ## 
## Part 1 ## 

import re

# Reading the input file for Day 3
file_path_day3 = 'inputday3.txt'

# Load the file
with open(file_path_day3, 'r') as file:
    corrupted_memory = file.read()

# Regular expression to extract valid mul(X,Y) instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches
matches = re.findall(pattern, corrupted_memory)

# Calculate the sum of the results
total_sum = sum(int(x) * int(y) for x, y in matches)
print("Part 1 answer : %s"%(total_sum))



## Part 2 ##

# Regular expressions for parsing
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Initialize variables
enabled = True  # mul instructions are enabled at the start
total_sum = 0

# Split the input into individual tokens
tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", corrupted_memory)

# Process each token
for token in tokens:
    token = token.strip()
    if not token:
        continue

    # Toggle states based on do() or don't()
    if re.match(do_pattern, token):
        enabled = True
    elif re.match(dont_pattern, token):
        enabled = False
    # Process mul instructions if enabled
    elif enabled and re.match(mul_pattern, token):
        x, y = map(int, re.findall(r"\d{1,3}", token))
        total_sum += x * y

print("Part 2 answer : %s"%(total_sum))
