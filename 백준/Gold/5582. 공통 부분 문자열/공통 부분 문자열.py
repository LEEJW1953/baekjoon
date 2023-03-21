import sys
input=sys.stdin.readline

s1=input().strip()
s2=input().strip()
n, m = len(s1), len(s2)
arr=[[0]*(m+1) for _ in range(n+1)]
answer=0
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1]==s2[j-1]:
            arr[i][j]=arr[i-1][j-1]+1
            answer=max(answer, arr[i][j])
        else:
            arr[i][j]=0
print(answer)