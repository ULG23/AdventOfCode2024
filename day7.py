## Day 7 ##

## Part 1 ## 

# Reading the input file for Day 7
file_path_day7 = 'inputday7.txt'

# Load the file
with open(file_path_day7, 'r') as file:
    input = file.read()


from itertools import product

def parse_input(input_data):
    """Parse the input into test values and corresponding numbers."""
    equations = []
    for line in input_data.strip().splitlines():
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        equations.append((test_value, numbers))
    return equations

def evaluate_equation(numbers, operators):
    """Evaluate the equation with the given numbers and operators."""
    result = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
    return result

def calculate_total_calibration_result(equations):
    """Calculate the total calibration result for valid equations."""
    total_calibration_result = 0

    for test_value, numbers in equations:
        n = len(numbers) - 1  # Number of operator slots
        valid = False

        # Generate all combinations of operators
        for operators in product(['+', '*'], repeat=n):
            if evaluate_equation(numbers, operators) == test_value:
                valid = True
                break

        if valid:
            total_calibration_result += test_value

    return total_calibration_result

# Parse input
equations = parse_input(input)

# Calculate total calibration result
total_result = calculate_total_calibration_result(equations)

print("Total Calibration Result:", total_result)


## Part 2 ##


def calculate_total_calibration_result_with_concat(equations):
    """Calculate the total calibration result for valid equations."""
    total_calibration_result = 0

    for test_value, numbers in equations:
        n = len(numbers) - 1  # Number of operator slots
        valid = False

        # Generate all combinations of operators
        for operators in product(['+', '*', '||'], repeat=n):
            if evaluate_equation(numbers, operators) == test_value:
                valid = True
                break

        if valid:
            total_calibration_result += test_value

    return total_calibration_result

# Parse input
equations = parse_input(input)

# Calculate total calibration result with concatenation
total_result = calculate_total_calibration_result_with_concat(equations)

print("Total Calibration Result with Concatenation:", total_result)