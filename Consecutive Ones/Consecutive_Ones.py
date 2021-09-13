# Return the longest run of 1s for a given integer n's binary representation.

# Example:

# Input: 242
# Output: 4

def longest_run(n):
    temp_str = bin(n)
    highest_count = 0
    current_count = 0
    for i in temp_str:
        if i == '1':
            current_count += 1
            if current_count > highest_count:
                highest_count = current_count
        else:
            if current_count > highest_count:
                highest_count = current_count
            current_count = 0

    return highest_count


print(longest_run(242))
