import sys
input=sys.stdin.readline
from itertools import combinations

arr=[]
for i in range(9):
    arr.append(int(input()))
arr.sort()
arr1=list(combinations(arr, 7))
for i in range(36):
    if sum(arr1[i])==100:
        for j in range(7):
            print(arr1[i][j])
        break