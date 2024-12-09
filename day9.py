## Day 9 ##
## Part 1 ##

# Reading the input file for Day 9
file_path_day9 = 'inputday9.txt'

# Load the file
with open(file_path_day9, 'r') as file:
    input_data = file.read()

def parse_disk_map(disk_map):
    """Parse the disk map into a list of blocks."""
    disk = []
    file_id = 0
    is_file = True  # Alternates between file and free space

    for length in map(int, disk_map):
        if is_file:
            disk.extend([file_id] * length)
            file_id += 1
        else:
            disk.extend(['.'] * length)
        is_file = not is_file

    return disk

def compact_disk(disk):
    """Compact the disk by moving file blocks left into free space."""
    # Find the leftmost free space
    free_space_index = 0
    while free_space_index < len(disk) and disk[free_space_index] != '.':
        free_space_index += 1

    # Move blocks from rightmost file to the leftmost free space
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != '.' and free_space_index < i:
            # Move block to the leftmost free space
            disk[free_space_index] = disk[i]
            disk[i] = '.'

            # Update free space index
            while free_space_index < len(disk) and disk[free_space_index] != '.':
                free_space_index += 1

def calculate_checksum(disk):
    """Calculate the checksum of the final disk state."""
    checksum = 0
    for position, block in enumerate(disk):
        if block != '.':
            checksum += position * block
    return checksum

# Parse the disk map
disk = parse_disk_map(input_data)

# Compact the disk
compact_disk(disk)

# Calculate the checksum
checksum = calculate_checksum(disk)

print("Filesystem Checksum:", checksum)

## Part 2 ##

def find_free_span(disk, length):
    """Find the leftmost span of free space of the given length."""
    free_start = None
    free_length = 0

    for i, block in enumerate(disk):
        if block == '.':
            if free_start is None:
                free_start = i
            free_length += 1
            if free_length == length:
                return free_start
        else:
            free_start = None
            free_length = 0

    return None


def compact_disk_whole_files(disk):
    """Compact the disk by moving whole files to the leftmost free space."""
    file_ids = sorted(set(block for block in disk if block != '.'), reverse=True)

    for file_id in file_ids:
        # Find the current location and length of the file
        indices = [i for i, block in enumerate(disk) if block == file_id]
        if not indices:
            continue
        file_length = len(indices)

        # Find the leftmost free span that can fit the file
        free_start = find_free_span(disk, file_length)

        if free_start is not None:
            # Move the file to the free span
            for i in indices:
                disk[i] = '.'
            for i in range(free_start, free_start + file_length):
                disk[i] = file_id



# Compact the disk using whole file compaction
compact_disk_whole_files(disk)

# Calculate the checksum
wholeChecksum = calculate_checksum(disk)

print("Filesystem Checksum:", checksum)