import sys
input=sys.stdin.readline

def find(x):
    if x!=people[x]:
        people[x]=find(people[x])
    return people[x]

def union(x, y):
    x=find(x)
    y=find(y)
    if x<y:
        people[y]=x
    else:
        people[x]=y

n, m = map(int, input().split())
truth=list(map(int, input().split()))
people=list(range(n+1))
arr=[]
for i in range(m):
    guest=list(map(int, input().split()))
    arr.append(guest[1:])
    for j in range(1, len(guest)):
        for k in range(1, len(guest)):
            union(guest[j], guest[k])
newtruth=[]
for i in range(truth[0]):
    newtruth.append(find(truth[i+1]))
count=0
for i in range(m):
    for j in range(len(arr[i])):
        if find(arr[i][j]) not in newtruth:
            count+=1
            break
print(count)