import sys
input=sys.stdin.readline

def roundNum(n):
    if n-int(n)>=0.5:
        return int(n)+1
    else:
        return int(n)

n=int(input())
arr=[int(input()) for _ in range(n)]
arr.sort()
t=roundNum(n*0.15)
arr=arr[t:n-t]
if arr:
    print(roundNum(sum(arr)/len(arr)))
else:
    print(0)