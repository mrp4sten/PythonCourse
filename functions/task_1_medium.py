def fibonacci(n):
    if n <= 0:
        print("Input should be positive integer.")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

# Test the function
print(fibonacci(10))