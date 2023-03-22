import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
s=input().strip()
count=0
tmp=''
for i in range(2*n+1):
    if i%2==0:
        tmp+='I'
    else:
        tmp+='O'
for i in range(m-2*n):
    if s[i:i+2*n+1]==tmp:
        count+=1
print(count)