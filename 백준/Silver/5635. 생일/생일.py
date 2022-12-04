import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(input().split())
arr.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(arr[-1][0])
print(arr[0][0])