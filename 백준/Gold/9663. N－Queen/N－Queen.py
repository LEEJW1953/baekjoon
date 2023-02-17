import sys
input=sys.stdin.readline

def f():
    global count
    if len(arr)==n:
        count+=1
        return
    for i in range(n):
        if check(i):
            arr.append(i)
            f()
            arr.pop()

def check(x):
    for i in range(len(arr)):
        if arr[i]==x or ((i+arr[i])==(len(arr)+x)) or ((i-arr[i])==(len(arr)-x)):
            return False
    return True

n=int(input())
count=0
arr=[]
f()
print(count)