import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 1
    orange_count = 0
    for index in apples:
        if index >= s-a and index <= (s-a) + (t-s):
            apple_count += 1
    for index in oranges:
        if index < 0 and abs(index) >= b-t and abs(index) <= (b-t) + (t-s):
            orange_count += 1
    print(apple_count)
    print(orange_count)
    
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    
    countApplesAndOranges(s, t, a, b, apples, oranges)
