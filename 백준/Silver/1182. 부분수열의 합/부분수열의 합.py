import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def f(x):
    global count
    if ans and (sum(ans)==s):
        count+=1
    for i in range(x+1, n):
        ans.append(arr[i])
        f(i)
        ans.pop()

n, s=map(int, input().split())
arr=list(map(int, input().split()))
ans=[]
count=0
f(-1)
print(count)