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

def bina(arr, st, en):
    mid=(st+en)//2
    if mid<=st:
        if give(arr, mid):
            return mid
        return 0
    if give(arr, mid):
        return bina(arr, mid, en)
    else:
        return bina(arr, st, mid)

m, n = map(int, input().split())
snack=list(map(int, input().split()))
snack.sort(reverse=True)
minn=1
maxx=max(snack)
print(bina(snack, minn, maxx+1))