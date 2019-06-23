# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
word, n = input().split()
word = sorted(word)
n = int(n)
answer = []
for i in range(1, n + 1):
    for item in sorted(list(combinations(word, i))):
        answer.append("".join(item))

print("\n".join(answer))
