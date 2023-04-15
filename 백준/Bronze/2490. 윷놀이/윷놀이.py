import sys
input=sys.stdin.readline
arr=['D','C','B','A','E']
for _ in range(3):
    n=sum(list(map(int, input().split())))
    print(arr[n])