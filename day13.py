# Reading the input file for Day 13
file_path_day13 = 'inputday13.txt'

# Load the file
with open(file_path_day13, 'r') as file:
    input_data = file.read().strip()

def parse_input(input_data):
    """Parse the input into a list of tuples."""
    machines = []
    lines = input_data.splitlines()
    
    for i in range(0, len(lines), 4):  # Process 4 lines at a time (A, B, Prize, empty line)
        line_a = lines[i]
        line_b = lines[i + 1]
        line_prize = lines[i + 2]
        
        # Extract values from the lines
        dx_A, dy_A = map(int, line_a.split('X+')[1].split(', Y+'))
        dx_B, dy_B = map(int, line_b.split('X+')[1].split(', Y+'))
        prize_x, prize_y = map(int, line_prize.split('X=')[1].split(', Y='))
        
        machines.append((dx_A, dy_A, dx_B, dy_B, prize_x, prize_y))
    
    return machines

def solve_claw_machine(dx_A, dy_A, dx_B, dy_B, prize_x, prize_y):
    """Solve for the minimum cost to win a single claw machine prize."""
    min_cost = float('inf')
    solution_found = False

    for a in range(101):  # Iterate over possible presses of button A
        for b in range(101):  # Iterate over possible presses of button B
            x = a * dx_A + b * dx_B
            y = a * dy_A + b * dy_B

            if x == prize_x and y == prize_y:
                solution_found = True
                cost = 3 * a + b  # Calculate cost
                min_cost = min(min_cost, cost)

    return min_cost if solution_found else None

def solve_all_machines(machines):
    """Solve for the minimum tokens to win all possible prizes."""
    total_cost = 0
    prizes_won = 0

    for machine in machines:
        dx_A, dy_A, dx_B, dy_B, prize_x, prize_y = machine
        cost = solve_claw_machine(dx_A, dy_A, dx_B, dy_B, prize_x, prize_y)
        if cost is not None:
            total_cost += cost
            prizes_won += 1

    return prizes_won, total_cost

# Parse the input
machines = parse_input(input_data)

# Solve
prizes_won, total_cost = solve_all_machines(machines)

print(f"Prizes won: {prizes_won}")
print(f"Total cost: {total_cost}")


## Part 2 ##

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to solve ax + by = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def solve_claw_machine(dx_A, dy_A, dx_B, dy_B, prize_x, prize_y):
    """Solve for the minimum cost to win a single claw machine prize."""
    g_x, x_A, x_B = extended_gcd(dx_A, dx_B)
    g_y, y_A, y_B = extended_gcd(dy_A, dy_B)

    # Check if solutions exist
    if prize_x % g_x != 0 or prize_y % g_y != 0:
        return None

    # Scale solutions to match prize_x and prize_y
    scale_x = prize_x // g_x
    scale_y = prize_y // g_y
    x_A *= scale_x
    x_B *= scale_x
    y_A *= scale_y
    y_B *= scale_y

    # Find combined solutions
    dx = dx_B // g_x
    dy = dy_B // g_y
    t_min, cost_min = None, float('inf')

    for t in range(-100, 101):  # Try integer adjustments to find minimal cost
        a = x_A + t * dx
        b = x_B - t * dx
        if a >= 0 and b >= 0:
            cost = 3 * a + b
            if cost < cost_min:
                t_min, cost_min = t, cost

    return cost_min if cost_min < float('inf') else None

def solve_all_machines(machines):
    """Solve for the minimum tokens to win all possible prizes."""
    total_cost = 0
    prizes_won = 0

    for machine in machines:
        dx_A, dy_A, dx_B, dy_B, prize_x, prize_y = machine
        cost = solve_claw_machine(dx_A, dy_A, dx_B, dy_B, prize_x, prize_y)
        if cost is not None:
            total_cost += cost
            prizes_won += 1

    return prizes_won, total_cost

def parse_input(input_data):
    """Parse the input into a list of tuples."""
    machines = []
    lines = input_data.strip().splitlines()
    
    for i in range(0, len(lines), 4):  # Process 4 lines at a time
        line_a = lines[i]
        line_b = lines[i + 1]
        line_prize = lines[i + 2]
        
        # Extract values from the lines
        dx_A, dy_A = map(int, line_a.split('X+')[1].split(', Y+'))
        dx_B, dy_B = map(int, line_b.split('X+')[1].split(', Y+'))
        prize_x, prize_y = map(int, line_prize.split('X=')[1].split(', Y='))
        
        # Adjust prize coordinates
        prize_x += 10**13
        prize_y += 10**13
        
        machines.append((dx_A, dy_A, dx_B, dy_B, prize_x, prize_y))
    
    return machines

# Read and parse input
machines = parse_input(input_data)

# Solve
prizes_won, total_cost = solve_all_machines(machines)

print(f"Prizes won: {prizes_won}")
print(f"Total cost: {total_cost}")