import sys
input=sys.stdin.readline

def dfs(i, num):
    global arr, op, minval, maxval
    if i==n:
        maxval=max(maxval, num)
        minval=min(minval, num)
        res.append(maxval)
        res.append(minval)
    else:
        if op[0]>0:
            op[0]-=1
            dfs(i+1, num+arr[i])
            op[0]+=1
        if op[1]>0:
            op[1]-=1
            dfs(i+1, num-arr[i])
            op[1]+=1
        if op[2]>0:
            op[2]-=1
            dfs(i+1, num*arr[i])
            op[2]+=1
        if op[3]>0:
            op[3]-=1
            dfs(i+1, int(num/arr[i]))
            op[3]+=1

n=int(input())
arr=list(map(int, input().split()))
op=list(map(int, input().split()))
minval=1e11
maxval=-1e11
res=[]
dfs(1, arr[0])
print(maxval)
print(minval)