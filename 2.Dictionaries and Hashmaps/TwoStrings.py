#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    first = {}
    second = {}
    for i in s1:
        if i in first.keys():
            first[i]+=1
        else:
            first[i]=1
    for i in s2:
        if i in second.keys():
            second[i]+=1
        else:
            second[i]=1
    for i in s1:
        if i in first.keys() and i in second.keys():
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
