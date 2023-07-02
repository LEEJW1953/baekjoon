import sys
input=sys.stdin.readline

def check(s):
    count1, count2 = 0, 0
    for i in range(len(s)):
        if s[i]=='W':
            count1+=1
        if s[i]=='B':
            count2+=1
        if count2>b:
            return 0
    if count1<w:
        return 1
    else:
        return 2

n, b, w = map(int, input().split())
g=input().strip()
ans=0
left, right = 0, 1
while left<n:
    s=g[left:right]
    tmp=check(s)
    if tmp==2:
        ans=max(ans, len(s))
        right+=1
    elif tmp==1:
        right+=1
    else:
        left+=1
    if right>n:
        right=n
        left+=1
print(ans)