# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
values = list(input().split())
is_palindromic = any(n[::-1] == n for n in values)
is_positive = all(int(i) > 0 for i in values)
print(is_palindromic & is_positive)
