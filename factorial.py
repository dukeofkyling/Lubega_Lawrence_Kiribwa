def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_iterative(n):
    """
    Calculate the factorial of a number using iteration.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calculate factorial of 5
number = 5

# Using recursive approach
result_recursive = factorial(number)
print(f"Factorial of {number} (recursive): {result_recursive}")

# Using iterative approach
result_iterative = factorial_iterative(number)
print(f"Factorial of {number} (iterative): {result_iterative}")

# Verification: 5! = 5 × 4 × 3 × 2 × 1 = 120
print(f"\nVerification: 5 × 4 × 3 × 2 × 1 = {5 * 4 * 3 * 2 * 1}")