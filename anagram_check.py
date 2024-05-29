#Write a function that checks if two given strings are anagrams (contain the same characters with the same frequencies).

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage:
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
