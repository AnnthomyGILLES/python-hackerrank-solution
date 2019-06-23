#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    """
     Function return an integer representing the number of occurrences 
     of 'a' in the prefix of length n in the infinitely repeating string s.
    """
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

