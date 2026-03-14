#!/usr/bin/env python3

# Sample dataset
data = [1, 2, 3, 4, 5]

# Calculate mean
mean = sum(data) / len(data)

# Sort data for median
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 1:
    median = sorted_data[n//2]
else:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2

# Mode (most frequent value)
from collections import defaultdict
freq = defaultdict(int)
for num in data:
    freq[num] += 1
mode = [k for k, v in freq.items() if v == max(freq.values())]

# Standard deviation
variance = sum((x - mean)**2 for x in data) / len(data)
std_dev = variance ** 0.5

# Output results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")