#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    n = len(c)
    i = 0
    while i < n-1:
        if ((i+2) <= (n-1)) and c[i+2] == 0:
            steps += 1
            i = i + 2
        elif ((i+1) <= (n-1)) and c[i+1] == 0:
            steps += 1
            i = i + 1
        else:
            i += 1
    return steps
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

