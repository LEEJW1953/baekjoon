import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))
arr.sort()
if n%2!=0:
    print((arr[(n-1)//2])**2)
else:
    print(arr[0]*arr[n-1])