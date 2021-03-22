import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    counter = 0
    for i in range(0,len(s)+1-m):
        if sum(s[i:i+m]) == d:
            counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()