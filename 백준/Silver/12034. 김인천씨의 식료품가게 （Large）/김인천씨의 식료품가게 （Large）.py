import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    arr1=[]
    for j in range(n):
        a=arr.pop()
        arr1.append(a*3//4)
        arr.remove(a*3//4)
    arr1.sort()
    s=' '.join(map(str, arr1))
    print(f'Case #{i+1}:',s)