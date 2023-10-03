import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(n-2):
    a, b, c = arr[i], arr[i+1], arr[i+2]
    if b+c>a:
        print(a+b+c)
        exit(0)
print(-1)