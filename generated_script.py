#!/usr/bin/env python3
data = [1, 2, 3, 4, 5]
mean = sum(data) / len(data)
median = data[len(data)//2]
mode = data
std_dev = (sum((x - mean)**2 for x in data) / len(data)) ** 0.5
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")