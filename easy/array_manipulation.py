#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import array
# Complete the arrayManipulation function below.

def is_overlap(a, b):
  return a[0] < b[1] and b[0] < a[1]
  
def looper(start, end):
    for i in range(start, end):
        yield i
def arrayManipulation(n, queries):
    arr = defaultdict(int)
    tmp_start = None
    tmp_end = None
    for item in queries:
        start, end, value = item
        start -= 1
        for i in looper(start, end):
            arr[i] += value
    return max(set(arr.values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

