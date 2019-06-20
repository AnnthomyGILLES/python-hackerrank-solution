#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    etape = 0
    for step in s:
        if step == 'D':
            etape -= 1
        elif step == 'U':
            if etape == -1:
                valley += 1
            etape +=1
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

