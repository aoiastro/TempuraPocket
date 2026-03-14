import itertools

fruits = ['apple', 'cherry', 'date', 'banana', 'elderberry']

for perm in itertools.permutations(fruits):
    print(' '.join(perm))