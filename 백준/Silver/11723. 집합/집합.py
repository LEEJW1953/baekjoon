import sys
input=sys.stdin.readline

s=[]
m=int(input())
for i in range(m):
    cal=list(map(str, input().split()))
    if len(cal)==2:
        cal[1]=int(cal[1])
    if cal[0]=='add':
        if cal[1] not in s:
            s.append(cal[1])
        else:
            continue
    elif cal[0]=='remove':
        if cal[1] in s:
            s.remove(cal[1])
        else:
            continue
    elif cal[0]=='check':
        if cal[1] in s:
            print(1)
        else:
            print(0)
    elif cal[0]=='toggle':
        if cal[1] in s:
            s.remove(cal[1])
        else:
            s.append(cal[1])
    elif cal[0]=='all':
        s=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    elif cal[0]=='empty':
        s=[]