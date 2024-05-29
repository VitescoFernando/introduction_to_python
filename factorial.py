#Write a function that calculates the factorial of a given non-negative integer.
'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
'''
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
n = 5
factorial = factorial_iterative(n)
print(f"The factorial of {n} is {factorial}")  # Output: The factorial of 5 is 120
