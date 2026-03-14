#!/usr/bin/env python3
import sys

# Generate data points with specified properties
data = [1, 2, 3, 4, 5]

# Calculate statistics
mean = sum(data) / len(data)
median = data[len(data) // 2]
mode = data
std_dev = (sum((x - mean)**2 for x in data) / len(data)) ** 0.5

# Output results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")