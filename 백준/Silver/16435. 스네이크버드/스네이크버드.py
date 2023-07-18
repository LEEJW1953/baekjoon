import sys
input=sys.stdin.readline

n, l = map(int, input().split())
arr=list(map(int, input().split()))
height=l
arr.sort()
while True:
    if arr:
        if height>=arr[0]:
            arr=arr[1:]
            height+=1
        else:
            break
    else:
        break
print(height)