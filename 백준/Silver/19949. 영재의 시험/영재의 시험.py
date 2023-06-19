import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def f(d):
    global result
    if d>5:
        count1=0
        for i in range(d):
            if ans[i]==arr[i]:
                count1+=1
        if count1<d-5:
            return
    if d==10:
        count=0
        for i in range(10):
            if ans[i]==arr[i]:
                count+=1
        if count>=5:
            result+=1
        return
    for i in range(1, 6):
        if d>1 and arr[d-2]==arr[d-1]==i:
            continue
        arr.append(i)
        f(d+1)
        arr.pop()

ans=list(map(int, input().split()))
arr=[]
result=0
f(0)
print(result)