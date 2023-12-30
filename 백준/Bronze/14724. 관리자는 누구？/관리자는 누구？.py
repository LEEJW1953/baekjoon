import sys
input=sys.stdin.readline

arr=['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
arr1=[]
n=int(input())
for i in range(9):
    tmp=list(map(int, input().split()))
    arr1.append(max(tmp))
print(arr[arr1.index(max(arr1))])