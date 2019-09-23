import numpy


def arrays(arr):
    # complete this function
    return numpy.array(arr, float)[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
