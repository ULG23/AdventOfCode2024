## Day 11 ##
## Part 1 ##

# Reading the input file for Day 11
file_path_day11 = 'inputday11.txt'

# Load and parse the file
with open(file_path_day11, 'r') as file:
    input_data = file.read().strip()

# Parse the input into a list of integers
stones = list(map(int, input_data.split()))

def split_number(number):
    """Split a number with an even number of digits into two parts."""
    digits = str(number)
    mid = len(digits) // 2
    return int(digits[:mid]), int(digits[mid:])

def simulate_blinks(stones, blinks):
    """Simulate the evolution of stones over a given number of blinks."""
    for _ in range(blinks):
        next_stones = []
        for stone in stones:
            if stone == 0:
                next_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                next_stones.extend([left, right])
            else:
                next_stones.append(stone * 2024)
        stones = next_stones
    return stones

# Simulate 25 blinks
final_stones_25 = simulate_blinks(stones, 25)

# Count the number of stones
print("Number of stones after 25 blinks:", len(final_stones_25))

## Part 2 ##
# Simulate 75 blinks
final_stones_75 = simulate_blinks(stones, 75)

# Count the number of stones
print("Number of stones after 25 blinks:", len(final_stones_75))