## Day 10 ##
## Part 1 ##

# Reading the input file for Day 10
file_path_day10 = 'inputday10.txt'

# Load the file
with open(file_path_day10, 'r') as file:
    input_map = file.read()

def parse_map(input_map):
    """Parse the input map into a 2D grid of integers."""
    return [[int(char) for char in line] for line in input_map.strip().splitlines()]

def bfs_trailhead_score(grid, start):
    """Perform BFS to calculate the score of a trailhead."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = [start]
    reached_nines = set()
    
    while queue:
        r, c = queue.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # If we reach a height of 9, add to the reached set
        if grid[r][c] == 9:
            reached_nines.add((r, c))
            continue

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] == grid[r][c] + 1:
                    queue.append((nr, nc))
    
    return len(reached_nines)

def calculate_trailhead_scores(grid):
    """Calculate the sum of scores of all trailheads."""
    rows, cols = len(grid), len(grid[0])
    total_score = 0
    
    # Find all trailheads (positions with height 0)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # Calculate the score for this trailhead
                total_score += bfs_trailhead_score(grid, (r, c))
    
    return total_score


# Parse the input map
grid = parse_map(input_map)

# Calculate the total score of all trailheads
total_score = calculate_trailhead_scores(grid)

print("Sum of trailhead scores:", total_score)


## Part 2 ##

def dfs_count_trails(grid, r, c, memo):
    """Perform DFS to count distinct hiking trails starting from a given position."""
    rows, cols = len(grid), len(grid[0])

    # Memoization check
    if (r, c) in memo:
        return memo[(r, c)]

    # If we reach a height of 9, this is the end of a trail
    if grid[r][c] == 9:
        return 1

    total_trails = 0

    # Explore neighbors
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c] + 1):
            total_trails += dfs_count_trails(grid, nr, nc, memo)

    # Memoize the result
    memo[(r, c)] = total_trails
    return total_trails

def calculate_trailhead_ratings(grid):
    """Calculate the sum of ratings of all trailheads."""
    rows, cols = len(grid), len(grid[0])
    total_rating = 0
    memo = {}

    # Find all trailheads (positions with height 0)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # Calculate the rating for this trailhead using DFS
                total_rating += dfs_count_trails(grid, r, c, memo)

    return total_rating


# Calculate the total rating of all trailheads
total_rating = calculate_trailhead_ratings(grid)

print("Sum of trailhead ratings:", total_rating)