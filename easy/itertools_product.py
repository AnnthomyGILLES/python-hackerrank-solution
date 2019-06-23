# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
A = input().split()
A = list(map(int, A))
B = input().split()
B = list(map(int, B))

for i in itertools.product(A, B):
    print(i, end=" ")


