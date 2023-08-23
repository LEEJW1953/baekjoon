import sys
input=sys.stdin.readline

n=int(input())
arr=[0]*26
for i in range(n):
    s=input().strip()
    arr[ord(s[0])-97]+=1
ans=''
for i in range(26):
    if arr[i]>=5:
        ans+=chr(97+i)
if ans:
    print(ans)
else:
    print('PREDAJA')