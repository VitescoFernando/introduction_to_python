# Write a function that takes two arrays and returns their intersection (elements common to both arrays).
# common elements between them

def array_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage:
print(array_intersection([1, 2, 2, 3], [2, 2, 3, 4]))  # Output: [2, 3]
