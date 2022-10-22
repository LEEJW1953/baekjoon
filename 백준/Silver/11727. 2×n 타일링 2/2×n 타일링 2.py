import sys
input=sys.stdin.readline

n=int(input())
arr=[]
arr.append(0)
arr.append(1)
arr.append(3)
if n>=3:
    for i in range(3, n+1):
        arr.append((arr[i-2]*2+arr[i-1])%10007)
print(arr[n])