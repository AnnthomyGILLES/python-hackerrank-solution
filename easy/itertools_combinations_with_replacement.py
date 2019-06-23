# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
word, n = input().split()
result = sorted([''.join(x) for x in combinations_with_replacement(sorted(word), int(n))])
for item in result:
    print(item)

