#!/usr/bin/env python3
import random

# Generate a random poem by selecting words from a predefined list
words = ["apple", "banana", "cherry", "date", "elderberry"]
poem = []
for i in range(5):
    line = " ".join(random.choices(words, k=5))
    poem.append(line)
print("\n".join(poem))