import sys
input=sys.stdin.readline

s=input().strip()
n=len(s)
arr=[]
for i in range(1, n-1):
    for j in range(i+1, n):
        arr.append(s[0:i][::-1]+s[i:j][::-1]+s[j:n][::-1])
arr.sort()
print(arr[0])