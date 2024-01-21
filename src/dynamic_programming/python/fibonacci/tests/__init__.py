def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
result = fibonacci(10)
print(result)
