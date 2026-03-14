#!/usr/bin/env python3
import random

# Generate a list of 100 random integers between 1 and 100
data = [random.randint(1, 100) for _ in range(100)]

# Calculate basic statistical measures
mean = sum(data) / len(data)
median = sorted(data)[len(data) // 2]
mode = max(set(data), key=lambda x: data.count(x))

# Output the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")