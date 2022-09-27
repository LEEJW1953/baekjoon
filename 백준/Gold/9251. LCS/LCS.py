import sys
input=sys.stdin.readline

aa=input().strip()
bb=input().strip()
a=len(aa)
b=len(bb)
arr=[[0]*(a+1) for _ in range(b+1)]
for j in range(1, a+1):
    for i in range(1, b+1):
        if aa[j-1]==bb[i-1]:
            arr[i][j]=arr[i-1][j-1]+1
        else:
            arr[i][j]=max(arr[i-1][j], arr[i][j-1])
print(max(arr[b]))