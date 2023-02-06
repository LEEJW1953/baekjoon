import sys
input=sys.stdin.readline

n=int(input())
arr={}
answer=[]
for i in range(n):
    a, b=map(str, input().split())
    arr[a]=b
for i in arr.keys():
    if arr[i]=="enter":
        answer.append(i)
answer.sort(reverse=True)
for i in range(len(answer)):
    print(answer[i])