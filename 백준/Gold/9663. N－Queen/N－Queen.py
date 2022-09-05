import sys
input=sys.stdin.readline

def check(x):
    for i in range(x):
        if arr[i]==arr[x] or abs((arr[i]-arr[x]))==abs(i-x):
            return False
    return True

def queen(x):
    global count
    if x==n:
        count+=1
    else:
        for i in range(n):
            arr[x]=i
            if check(x):
                queen(x+1)


n=int(input())
arr=[0]*n
count=0
queen(0)
print(count)