## Day 8 ## 

## Part 1 ##

# Reading the input file for Day 8
file_path_day8 = 'inputday8.txt'

# Load the file
with open(file_path_day8, 'r') as file:
    input_map = file.read()

def parse_map(input_map):
    """Parse the map to identify antenna positions and frequencies."""
    grid = input_map.strip().splitlines()
    antennas = {}
    
    # Find all antennas and their positions
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((r, c))
    print("Parsed Antennas:", antennas)  # Debugging
    return grid, antennas

def calculate_antinodes(antennas, rows, cols):
    """Calculate the unique locations of all antinodes."""
    antinodes = set()
    
    for freq, positions in antennas.items():
        # Compare each pair of antennas of the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                
                # Calculate the midpoint and distance
                mr, mc = (r1 + r2) // 2, (c1 + c2) // 2
                dr, dc = r2 - r1, c2 - c1
                
                print(f"Checking Pair ({r1},{c1}) and ({r2},{c2})")  # Debugging
                
                # Check the antinode conditions
                if abs(dr) % 2 == 0 and abs(dc) % 2 == 0:
                    # Antinodes are at (mr - dr/2, mc - dc/2) and (mr + dr/2, mc + dc/2)
                    antinode1 = (mr - dr // 2, mc - dc // 2)
                    antinode2 = (mr + dr // 2, mc + dc // 2)
                    
                    print(f"Antinode Candidates: {antinode1}, {antinode2}")  # Debugging
                    
                    # Add valid antinodes within bounds
                    if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                        antinodes.add(antinode1)
                    if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                        antinodes.add(antinode2)
    
    print("Calculated Antinodes:", antinodes)  # Debugging
    return antinodes

def count_unique_antinodes(input_map):
    """Count the number of unique locations containing antinodes."""
    grid, antennas = parse_map(input_map)
    rows, cols = len(grid), len(grid[0])
    antinodes = calculate_antinodes(antennas, rows, cols)
    return len(antinodes)

# Calculate unique antinodes
unique_antinodes = count_unique_antinodes(input_map)
print("Unique locations with antinodes:", unique_antinodes)