# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
for i in range(int(input())):
    method_name, *value = input().split()
    if not value:
        _ = getattr(d, method_name)()
    else:
        getattr(d, method_name)(value)

print(' '.join(r for v in d for r in v))