import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
arrow=[0]*1000001
ans=0
for i in range(n):
    if arrow[arr[i]]:
        arrow[arr[i]-1]+=1
        arrow[arr[i]]-=1
    else:
        arrow[arr[i]-1]+=1
        ans+=1
print(ans)