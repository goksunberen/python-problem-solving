import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_counter = 0
    min_counter = 0
    min_value = scores[0]
    max_value = scores[0]
    for score in scores:
        if score > max_value:
            max_counter += 1
            max_value = score
        if score < min_value:
            min_counter += 1
            min_value = score
    array = [max_counter,min_counter]
    return array
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()