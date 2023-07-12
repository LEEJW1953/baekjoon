import sys
input=sys.stdin.readline

n, k = map(int, input().split())
arr=[]
for i in range(k):
    arr.append(int(str((i+1)*n)[::-1]))
print(max(arr))