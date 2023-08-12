import sys
input=sys.stdin.readline

n=int(input())
arr=[input().strip() for _ in range(n)]
if n!=1:
    st, en = '', ''
    for i in range(n):
        if arr[i]=='?':
            if i==0:
                en=arr[i+1][0]
            elif i==n-1:
                st=arr[i-1][-1]
            else:
                st=arr[i-1][-1]
                en=arr[i+1][0]
m=int(input())
arr1=[input().strip() for _ in range(m)]
if m==1:
    print(arr1[0])
else:
    ans=''
    for i in range(m):
        if st and en:
            if st==arr1[i][0] and en==arr1[i][-1]:
                if arr1[i] not in arr:
                    ans=arr1[i]
        else:
            if st and arr1[i][0]==st:
                if arr1[i] not in arr:
                    ans=arr1[i]
            if en and arr1[i][-1]==en:
                if arr1[i] not in arr:
                    ans=arr1[i]
    print(ans)