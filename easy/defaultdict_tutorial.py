# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())

result = defaultdict(list)
for i in range(1, n + 1):
    word = input()
    result[word].append(str(i))

for i in range(m):
    word = input()
    print(' '.join(result[word]) or -1)
