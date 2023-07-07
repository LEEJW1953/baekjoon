import sys
input=sys.stdin.readline

s=input().strip()
arr=[]
stack=[]
count=0
ans=[]
for i in s:
    if i=='(':
        count+=1
        arr.append((i, count))
        stack.append(count)
    elif i==')':
        arr.append((i, stack.pop()))
    else:
        arr.append((i, 0))
maxlen=len(bin(2**count)[2:])
for i in range(2**count-1):
    num=bin(i)[2:].zfill(maxlen-1)
    formula=''
    for j in arr:
        if not j[1]:
            formula+=j[0]
        else:
            if int(num[j[1]-1]):
                formula+=j[0]
    ans.append(formula)
ans=list(set(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])