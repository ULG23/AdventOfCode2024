## Day 4 ##
## Part 1 ## 


file_path_day4= 'inputday4.txt'

# Load the file
with open(file_path_day4, 'r') as file:
    grid = file.read().splitlines()

# Word to search for
word = "XMAS"
word_len = len(word)
rows, cols = len(grid), len(grid[0])

def count_word(grid, word):
    count = 0
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    
    # Directions: (row step, col step)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal ↘️
        (-1, -1),  # Diagonal ↖️
        (1, -1),  # Diagonal ↙️
        (-1, 1),  # Diagonal ↗️
    ]
    
    # Function to check a word in a specific direction
    def match(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True
    
    # Iterate over all starting points in the grid
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if match(r, c, dr, dc):
                    count += 1
    
    return count

# Count occurrences of "XMAS"
xmas_count = count_word(grid, word)
print("Part 1 : %s" %(xmas_count))


## Part 2 ##
def count_xmas_pattern(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    seen_patterns = set()  # Track unique patterns by their cell positions

    # Function to check the X-MAS pattern in a 3x3 grid starting at (r, c)
    def is_xmas(r, c):
        # Ensure within bounds
        if r + 2 >= rows or c + 2 >= cols:
            return False
        # Extract diagonals for the X-MAS pattern
        top_left = [(r, c), (r+1, c+1), (r+2, c+2)]  # Top-left to bottom-right
        top_right = [(r+2, c), (r+1, c+1), (r, c+2)]  # Bottom-left to top-right
        
        # Check if both diagonals form "MAS"
        if (sorted(grid[x][y] for x, y in top_left) == ["A", "M", "S"] and
            sorted(grid[x][y] for x, y in top_right) == ["A", "M", "S"]):
            return top_left + top_right
        return None

    # Iterate over all possible 3x3 subgrids
    for r in range(rows - 2):
        for c in range(cols - 2):
            pattern = is_xmas(r, c)
            if pattern:
                # Avoid duplicate patterns
                unique_pattern = tuple(sorted(pattern))
                if unique_pattern not in seen_patterns:
                    seen_patterns.add(unique_pattern)
                    count += 1

    return count

# Count X-MAS patterns
xmas_count = count_xmas_pattern(grid)
print("Part 2  : %s" % xmas_count)