## Day 5 ##

## Part 1 ##

# Reading the input file for Day 5
file_path_day5 = 'inputday5.txt'

# Load the file
with open(file_path_day5, 'r') as file:
    data = file.read()

def parse_input(input_data):
    """Parses input into rules and updates."""
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    return rules, updates

def is_update_valid(update, rules):
    """Checks if an update is valid based on the rules."""
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):  # x must appear before y
                return False
    return True

def calculate_middle_pages_sum(rules, updates):
    """Calculates the sum of middle pages for valid updates."""
    valid_updates = [update for update in updates if is_update_valid(update, rules)]
    middle_pages = [update[len(update) // 2] for update in valid_updates]  # Middle page of each valid update
    return sum(middle_pages)

# Process input
rules, updates = parse_input(data)

# Calculate result
result = calculate_middle_pages_sum(rules, updates)
print("Sum of middle pages:", result)


## Part 2 ##

from collections import defaultdict, deque

def topological_sort(pages, rules):
    """Sorts the pages based on the rules using topological sorting."""
    # Create graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build graph from applicable rules
    pages_set = set(pages)
    for x, y in rules:
        if x in pages_set and y in pages_set:
            graph[x].append(y)
            in_degree[y] += 1

    # Initialize queue with nodes having in-degree 0
    queue = deque([page for page in pages if in_degree[page] == 0])

    # Perform topological sorting
    sorted_pages = []
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

def correct_updates(rules, updates):
    """Corrects the order of incorrectly-ordered updates."""
    corrected_updates = []
    for update in updates:
        if not is_update_valid(update, rules):
            corrected_updates.append(topological_sort(update, rules))
    return corrected_updates

def calculate_corrected_middle_pages_sum(rules, updates):
    """Calculates the sum of middle pages for corrected updates."""
    corrected_updates = correct_updates(rules, updates)
    middle_pages = [update[len(update) // 2] for update in corrected_updates]
    return sum(middle_pages)


# Process input
rules, updates = parse_input(data)

# Calculate result
result = calculate_corrected_middle_pages_sum(rules, updates)
print("Sum of middle pages for corrected updates:", result)