import sys
input=sys.stdin.readline

def f(x, c1, c2):
    q=''
    if len(s)==l and 1<=c1 and 2<=c2:
        print(''.join(s))
    for i in range(x, c):
        if arr[i]!=q:
            if arr[i] in v:
                c1+=1
            else:
                c2+=1
            s.append(arr[i])
            q=arr[i]
            f(i+1, c1, c2)
            tmp=s.pop()
            if tmp in v:
                c1-=1
            else:
                c2-=1

l, c=map(int, input().split())
arr=list(input().split())
arr.sort()
v=['a','e','i','o','u']
s=[]
count1, count2 = 0, 0
f(0, 0, 0)