import sys
input=sys.stdin.readline

def give(arr, mid):
    count=0
    for i in range(n):
        count+=(arr[i]//mid)
        if count>=m:
            return True
    else:
        return False

m, n = map(int, input().split())
snack=list(map(int, input().split()))
snack.sort(reverse=True)
minn=1
maxx=max(snack)
while minn<=maxx:
    mid=(minn+maxx)//2
    if give(snack, mid):
        minn=mid+1
    else:
        maxx=mid-1
print(maxx)