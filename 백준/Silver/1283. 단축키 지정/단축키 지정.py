import sys
input=sys.stdin.readline

n=int(input())
d={}
for i in range(n):
    s=input().strip()
    arr=s.split()
    first=False
    idx=None
    for j in range(len(arr)):
        tmp=arr[j][0].upper()
        if tmp not in d:
            d[tmp]=arr[j][0]
            idx=j
            first=True
            break
    if not first:
        for j in range(len(s)):
            if s[j]==' ':
                continue
            tmp=s[j].upper()
            if tmp not in d:
                d[tmp]=s[j]
                idx=j
                break
    if first:
        for j in range(len(arr)):
            if j==idx:
                print(f'[{arr[j][0]}]', end='')
                print(arr[j][1:], end=' ')
            else:
                print(arr[j], end=' ')
    else:
        for j in range(len(s)):
            if j==idx:
                print(f'[{s[j]}]', end='')
            else:
                print(s[j], end='')
    print()