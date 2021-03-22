import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    for index in arr:
        if index > 0:
            pos_count = pos_count + 1
        elif index < 0:
            neg_count = neg_count + 1
        else:
            zero_count = zero_count + 1
    sum = pos_count + neg_count + zero_count
    print("{:.6f}".format(pos_count/sum))
    print("{:.6f}".format(neg_count/sum))
    print("{:.6f}".format(zero_count/sum))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)