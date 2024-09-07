def compose_pipeline(*functions):
    def composed_function(x):
        for func in functions:
            x = func(x)  # Apply each function in sequence to the input
        return x
    return composed_function


def add_one(x):
    return x + 1

def square(x):
    return x * x

def double(x):
    return x * 2

# Compose the functions in a pipeline
pipeline = compose_pipeline(add_one, square, double)

# Apply the composed function
result = pipeline(3)  # ((3 + 1) ** 2) * 2
print(result)  # Outputs: 32



def power_sequence(n, k):
    total = 0
    for i in range(1, k + 1):
        total += n ** i  # Add n raised to the power of i to the total
    return total

print(power_sequence(2, 3))  # Output: 14 (2^1 + 2^2 + 2^3 = 2 + 4 + 8 = 14)
print(power_sequence(3, 4))  # Output: 120 (3^1 + 3^2 + 3^3 + 3^4 = 3 + 9 + 27 + 81 = 120)
