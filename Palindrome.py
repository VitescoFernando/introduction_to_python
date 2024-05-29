#Write a function that checks if a given string is a palindrome (reads the same forward and backward).

def is_palindrome(s):
    # s[::-1] is used to reverse a sequence. This sequence can be a string, list, tuple, or any other iterable
    return s == s[::-1]

# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False