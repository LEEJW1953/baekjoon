import sys
input=sys.stdin.readline

def toggle(arr, x):
    if x==0:
        arr[0]=str(abs(1-int(arr[0])))
        arr[1]=str(abs(1-int(arr[1])))
    elif x==n-1:
        arr[n-1]=str(abs(1-int(arr[n-1])))
        arr[n-2]=str(abs(1-int(arr[n-2])))
    else:
        arr[x-1]=str(abs(1-int(arr[x-1])))
        arr[x]=str(abs(1-int(arr[x])))
        arr[x+1]=str(abs(1-int(arr[x+1])))
    return arr

n=int(input())
state1=list(input().strip())
state2=state1[:]
goal=input().strip()
if n==2:
    if ''.join(state1)==goal:
        print(0)
    else:
        state1=toggle(state1, 0)
        if ''.join(state1)==goal:
            print(1)
        else:
            print(-1)
    exit(0)
count1=0
count2=1
tmp1=False
tmp2=False
answer=1e9
state2=toggle(state2, 0)
for i in range(n):
    if i==n-1:
        if state1[i]==goal[i]:
            tmp1=True
        if state2[i]==goal[i]:
            tmp2=True
    else:
        if state1[i]!=goal[i]:
            state1=toggle(state1, i+1)
            count1+=1
        if state2[i]!=goal[i]:
            state2=toggle(state2, i+1)
            count2+=1
if tmp1:
    answer=count1
if tmp2:
    answer=min(answer, count2)
print(answer if answer!=1e9 else -1)