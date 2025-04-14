def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

numbers = [10, 20, 30, 40, 50]
result = 0
for num in numbers:
    result += num
    print(f"Intermediate result: {result} (added {num})")

def factorial(n):
    """
    Calculate the factorial of a given number n using recursion.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
