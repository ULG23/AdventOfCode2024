## part 1 ##

# Reading the input file and parsing the data
file_path = 'inputday1.txt'

# Load the file
with open(file_path, 'r') as file:
    data = file.readlines()

# Parse the two lists
left_list, right_list = [], []

for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Sorting both lists
left_list.sort()
right_list.sort()

# Calculate the total distance
total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
print(total_distance)



## part 2 ##

from collections import Counter

# Count occurrences of each number in the right list
right_count = Counter(right_list)

# Calculate the similarity score
similarity_score = sum(left * right_count[left] for left in left_list)
print(similarity_score)