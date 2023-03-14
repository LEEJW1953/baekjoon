import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    s=input().strip()
    arr=[0]*26
    tmp=True
    for i in range(len(s)):
        arr[ord(s[i])-65]+=1
        if arr[ord(s[i])-65] and arr[ord(s[i])-65]%3==0:
            if i==len(s)-1:
                tmp=False
                break
            elif s[i+1]!=s[i]:
                tmp=False
                break
            arr[ord(s[i])-65]=-1
    if tmp:
        print('OK')
    else:
        print('FAKE')