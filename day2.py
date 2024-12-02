#day2 solution for advent of code 2024 
## Part 1 ##

# Reading the input file for Day 2
file_path_day2 = 'inputday2.txt'

# Load the file
with open(file_path_day2, 'r') as file:
    reports = file.readlines()

levels = 0

def is_safe(report):
    levels = list(map(int, report.split()))
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    # Check all differences are within the range [1, 3] or [-1, -3]
    if all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences):
        return True
    return False

# Count safe reports
safe_reports_count = sum(1 for report in reports if is_safe(report))
print(safe_reports_count)

## Part 2 ##

def is_safe_with_dampener(report):
    levels = list(map(int, report.split()))
    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    
    # Check if the original report is safe
    if all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences):
        return True
    
    # Check by removing one level at a time
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        modified_differences = [modified_levels[j+1] - modified_levels[j] for j in range(len(modified_levels) - 1)]
        if all(1 <= diff <= 3 for diff in modified_differences) or all(-3 <= diff <= -1 for diff in modified_differences):
            return True
    
    return False

# Count safe reports considering the Problem Dampener
safe_reports_with_dampener_count = sum(1 for report in reports if is_safe_with_dampener(report))
print(safe_reports_with_dampener_count)