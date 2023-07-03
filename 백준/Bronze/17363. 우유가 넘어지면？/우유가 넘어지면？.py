import sys
input=sys.stdin.readline

n, m = map(int, input().split())
arr=[list(input().strip()) for _ in range(n)]
ans=[]
d={46:46,
    79:79,
    45:124,
    124:45,
    47:92,
    92:47,
    94:60,
    60:118,
    118:62,
    62:94}
for i in range(m-1, -1, -1):
    tmp=[]
    for j in range(n):
        tmp.append(chr(d[ord(arr[j][i])]))
    ans.append(tmp)
for i in range(m):
    print(''.join(ans[i]))