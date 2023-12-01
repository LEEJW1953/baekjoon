import sys
input=sys.stdin.readline

def next_permutation(arr):
    i=len(arr)-1
    while i and arr[i]<=arr[i-1]:
        i-=1
    if not i:
        return arr
    j=len(arr)-1
    while arr[j]<=arr[i-1]:
        j-=1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    j=len(arr)-1
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr

t=int(input())
for _ in range(t):
    s=list(map(str, input().strip()))
    arr=next_permutation(s)
    print(''.join(arr))