def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        memo (dict): A dictionary to store previously computed results.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = result
        return result

print(fibonacci(10))

numbers = [10, 20, 30, 40, 50]
result = 0
for num in numbers:
    result += num
    print(f"Intermediate result: {result} (added {num})")

def factorial(n):
    """
    Calculate the factorial of a given number n using an iterative approach.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
