import sys
input=sys.stdin.readline

s=input().strip()
arr=[0]*26
ans=''
tmp=True
mid=0
for i in s:
    arr[ord(i)-65]+=1
for i in range(26):
    if arr[i]==0:
        continue
    if arr[i]%2==1:
        if tmp:
            tmp=False
            mid=chr(i+65)
            for j in range(arr[i]//2):
                ans+=chr(i+65)
        else:
            print("I'm Sorry Hansoo")
            exit(0)
    else:
        for j in range(arr[i]//2):
            ans+=chr(i+65)
if mid!=0:
    ans+=mid
for i in range(25, -1, -1):
    for j in range(arr[i]//2):
        ans+=chr(i+65)
print(ans)