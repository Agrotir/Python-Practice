# Given a non-empty array where each element represents a digit of a non-negative integer,
# add one to the integer. The most significant digit is at the front of the array and each
# element in the array contains only one digit. Furthermore, the integer does not have
# leading zeros, except in the case of the number '0'.

# Example:
# Input: [2,3,4]
# Output: [2,3,5]

class Solution():
    def plusOne(self, digits):
        i = len(digits) - 1
        while digits[i] == 9:
            digits[i] = 0
            if i == 0:
                break
            i -= 1
        if i == 0 and digits[i] == 0:
            digits.insert(0, 1)
        else:
            digits[i] += 1
        return digits


num = [2, 9, 9]
print(num)
print(Solution().plusOne(num))
