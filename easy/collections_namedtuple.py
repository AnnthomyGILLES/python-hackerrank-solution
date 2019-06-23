# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
Student = namedtuple("Student", input().split())

sum = 0
for i in range(n):
    line = input().split()
    student = Student(*line)
    sum += int(student.MARKS)

print(sum/n)
