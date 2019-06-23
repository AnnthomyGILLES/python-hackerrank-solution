# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = list(map(int, input().split()))

students = []
for i in range(x):
    students.append(list(map(float, input().split())))

for notation in zip(*students):
    print(sum(notation)/x)
