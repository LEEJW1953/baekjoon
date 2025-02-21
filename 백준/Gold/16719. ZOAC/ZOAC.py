import sys

input = sys.stdin.readline

s = input().strip()
n = len(s)
ans = [""] * n
idx = 0
d = {}
for i in range(len(s)):
    d[i] = s[i]
while d:
    idx = 0
    for i in range(n):
        if i in d:
            ans[i] = d[i]
            idx = i
            tmp = "".join(ans)
            ans[i] = ""
            break
    for i in range(n):
        if i not in d or idx == i:
            continue
        ans[i] = d[i]
        tmp1 = "".join(ans)
        ans[i] = ""
        if tmp1 < tmp:
            idx = i
            tmp = tmp1
    ans[idx] = d[idx]
    print("".join(ans))
    d.pop(idx)