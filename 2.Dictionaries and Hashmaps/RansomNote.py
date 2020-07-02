#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mydict = {}
    for i in magazine:
        if i in mydict.keys():
            mydict[i]+=1
        else:
            mydict[i]=1
    notedic = {}
    for i in note:
        if i in notedic.keys():
            notedic[i]+=1
        else:
            notedic[i]=1
    for i in note:
        if i not in mydict.keys():
            print("No")
            return
        if notedic[i]>mydict[i]:
            print("No")
            return
    print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
