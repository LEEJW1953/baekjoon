import sys
input=sys.stdin.readline

ans=''
arr=[input().strip() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if len(arr[j])>i:
            ans+=arr[j][i]
print(ans)