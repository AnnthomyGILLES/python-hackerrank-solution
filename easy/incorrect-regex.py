# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


n = int(input())

for i in range(n):
    print(is_valid_regex(input()))
