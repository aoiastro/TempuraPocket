#!/usr/bin/env python3

fruits = ['apple', 'cherry', 'date', 'banana', 'elderberry']

def generate_permutations():
    permutations = []
    used = [False] * len(fruits)
    def backtrack(start, path):
        if len(path) == len(fruits):
            permutations.append(path.copy())
            return
        for i in range(len(fruits)):
            if not used[i]:
                used[i] = True
                path.append(fruits[i])
                backtrack(i + 1, path)
                path.pop()
                used[i] = False
    backtrack(0, [])
    return permutations

for perm in generate_permutations():
    print(' '.join(perm))