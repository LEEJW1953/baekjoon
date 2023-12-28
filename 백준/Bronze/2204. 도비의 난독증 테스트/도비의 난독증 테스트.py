import sys
input=sys.stdin.readline

while True:
    n=int(input())
    if not n:
        break
    arr=[]
    for i in range(n):
        arr.append(input().strip())
    arr.sort(key=lambda x:x.lower())
    print(arr[0])