#Write a function that takes an array of integers and returns the second largest element. If there is no such element, return None.

def second_largest(nums):
    if len(nums) < 2:
        return None
    
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
            
    return second if second != float('-inf') else None

# Example usage:
print(second_largest([1, 3, 4, 5, 0, 2]))  # Output: 4
print(second_largest([7, 7, 7]))  # Output: None
