## Day 6 ##

## Part 1 ##

# Reading the input file for Day 6
file_path_day6 = 'inputday6.txt'

# Load the file
with open(file_path_day6, 'r') as file:
    input = file.read()


def predict_guard_path(map_lines):
    # Parse the input map into a 2D list
    grid = [list(line) for line in map_lines]
    
    # Find the starting position and direction of the guard
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    reverse_directions = {v: k for k, v in directions.items()}

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_pos = (r, c)
                guard_dir = directions[cell]
                grid[r][c] = '.'  # Clear the guard's starting position
                break

    visited = set()
    rows, cols = len(grid), len(grid[0])

    while True:
        visited.add(guard_pos)
        r, c = guard_pos
        dr, dc = guard_dir

        # Compute the next position
        next_r, next_c = r + dr, c + dc

        # Check if the next position is out of bounds or blocked
        if not (0 <= next_r < rows and 0 <= next_c < cols) or grid[next_r][next_c] == '#':
            # Turn right (change direction clockwise)
            guard_dir = (guard_dir[1], -guard_dir[0])
        else:
            # Move forward
            guard_pos = (next_r, next_c)

        # Stop if the guard is out of bounds
        if not (0 <= guard_pos[0] < rows and 0 <= guard_pos[1] < cols):
            break

    return len(visited)




result = predict_guard_path(input)
print(f"Number of distinct positions visited: {result}")