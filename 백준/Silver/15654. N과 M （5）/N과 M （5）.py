import sys
input=sys.stdin.readline

n, m=map(int, input().split())
num=list(map(int, input().split()))
num.sort()

arr=[]
def f():
    if len(arr)==m:
        print(' '.join(map(str, arr)))
        return

    for i in num:
        if i in arr:
            continue
        arr.append(i)
        f()
        arr.pop()
f()