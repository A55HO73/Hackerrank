"""problem link https://www.hackerrank.com/challenges/summing-the-n-series/problem"""

#!/bin/python3

import os
import sys

#
# Complete the summingSeries function below.
c = 10**9+7
def summingSeries(n):
    return (n%c)*(n%c)%c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
