import sys
input=sys.stdin.readline

n=int(input())
arr=[int(input()) for _ in range(n)]
left, right = 0, 0
ans1, ans2 = 0, 0
for i in range(n):
    tmp1, tmp2 = arr[i], arr[-1-i]
    if left<tmp1:
        ans1+=1
        left=tmp1
    if right<tmp2:
        ans2+=1
        right=tmp2
print(ans1)
print(ans2)