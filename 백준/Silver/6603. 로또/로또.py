import sys
input=sys.stdin.readline
from itertools import combinations

while True:
    arr=list(map(int, input().split()))
    k=arr[0]
    if k==0:
        break
    arr1=list(combinations(arr[1:], 6))
    # print(arr1)
    for i in combinations(arr[1:], 6):
        print(' '.join(list(map(str, i))))
    print()