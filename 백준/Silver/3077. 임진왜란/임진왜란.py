import sys
input=sys.stdin.readline

n=int(input())
answer=list(map(str, input().split()))
arr=list(map(str, input().split()))
dict1={}
dict2={}
score=0
for i in range(n):
    dict1[answer[i]]=i
for i in range(n):
    for j in range(i+1, n):
        if dict1[arr[i]] < dict1[arr[j]]:
            score+=1
print(f'{score}/{n*(n-1)//2}')