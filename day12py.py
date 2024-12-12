## Day 12 ##
## Part 1 ##

# Reading the input file for Day 12
file_path_day12 = 'inputday12.txt'

# Load the file
with open(file_path_day12, 'r') as file:
    input_data = file.read()

def parse_map(input_map):
    """Parse the input map into a 2D grid."""
    return [list(line) for line in input_map.strip().splitlines()]

def flood_fill(grid, visited, r, c, plant_type):
    """Perform flood fill to calculate the area and perimeter of a region."""
    rows, cols = len(grid), len(grid[0])
    area = 0
    perimeter = 0
    stack = [(r, c)]
    visited.add((r, c))

    while stack:
        x, y = stack.pop()
        area += 1

        # Check neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == plant_type and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
                elif grid[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1  # Out of bounds adds to the perimeter

    return area, perimeter

def calculate_total_price(grid):
    """Calculate the total price of fencing all regions on the map."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant_type = grid[r][c]
                area, perimeter = flood_fill(grid, visited, r, c, plant_type)
                total_price += area * perimeter

    return total_price


# Parse the input map
grid = parse_map(input_data)

# Calculate the total price of fencing
total_price = calculate_total_price(grid)

print("Total price of fencing:", total_price)


## Part 2 ##

def flood_fill_count_sides(grid, visited, r, c, plant_type):
    """Perform flood fill to calculate the area and number of sides of a region."""
    rows, cols = len(grid), len(grid[0])
    area = 0
    sides = 0
    stack = [(r, c)]
    visited.add((r, c))

    while stack:
        x, y = stack.pop()
        area += 1

        # Check neighbors and count sides
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == plant_type and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
                elif grid[nx][ny] != plant_type:
                    sides += 1
            else:
                sides += 1  # Out-of-bounds adds to the sides

    return area, sides

def calculate_total_price_with_sides(grid):
    """Calculate the total price of fencing all regions using sides."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                plant_type = grid[r][c]
                area, sides = flood_fill_count_sides(grid, visited, r, c, plant_type)
                total_price += area * sides

    return total_price

    # Parse the input map
grid = parse_map(input_data)

# Calculate the new total price of fencing
total_price = calculate_total_price_with_sides(grid)

print("New total price of fencing:", total_price)

