import sys
input=sys.stdin.readline

k=int(input())
for i in range(k):
    arr=list(map(int, input().split()))
    score=arr[1:]
    score.sort()
    diff=0
    for j in range(arr[0]-1):
        diff=max(diff, abs(score[j]-score[j+1]))
    print(f'Class {i+1}')
    print(f'Max {score[-1]}, Min {score[0]}, Largest gap {diff}')