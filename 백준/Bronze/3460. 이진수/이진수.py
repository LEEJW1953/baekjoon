import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    i=2
    while n!=0:
        arr.append(n%i)
        n-=n%i
        i*=2
    for j in range(len(arr)):
        if arr[j]:
            print(j, end=' ')
    print()