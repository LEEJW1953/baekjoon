import sys
input=sys.stdin.readline

s=input()
count=0
tmp=s[0]
for i in s:
    if i!=tmp:
        count+=1
        tmp=i
print(count//2)