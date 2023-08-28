import sys
input=sys.stdin.readline

def luck(tmp, x):
    global count, s
    if x==len(s):
        count+=1
    for i in d.keys():
        if i==tmp:
            continue
        if d[i]:
            d[i]-=1
            luck(i, x+1)
            d[i]+=1

s=input().strip()
count=0
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
luck('', 0)
print(count)