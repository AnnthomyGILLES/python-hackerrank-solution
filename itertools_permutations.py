# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
word, n = input().split()

for item in sorted(list(permutations(word, int(n)))):
    print("".join(item))

