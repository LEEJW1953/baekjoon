import sys
input=sys.stdin.readline

n=int(input())
arr=[0, 1]
for i in range(2, abs(n)+1):
    arr.append((arr[i-2]+arr[i-1])%1000000000)
if n%2==0 and n<0:
    print(-1)
elif n==0:
    print(0)
else:
    print(1)
print(arr[abs(n)])