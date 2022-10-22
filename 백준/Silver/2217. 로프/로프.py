import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
result=0
for i in range(n):
    result=max(result, (n-i)*arr[i])
print(result)