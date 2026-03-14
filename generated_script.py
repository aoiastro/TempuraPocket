import itertools

words = ['apple', 'cherry', 'date', 'banana', 'elderberry']

for perm in itertools.permutations(words):
    print(' '.join(perm))