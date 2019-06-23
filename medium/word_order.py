# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n = int(input())

d = defaultdict(int)

for i in range(n):
    word = input()
    d[word] += 1

print(len(d.keys()))
print(" ".join(map(str, d.values())))
