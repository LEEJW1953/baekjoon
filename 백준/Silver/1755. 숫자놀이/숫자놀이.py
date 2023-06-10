import sys
input=sys.stdin.readline

m, n = map(int, input().split())
text = ['zero','one','two','three','four','five','six','seven','eight','nine']
arr=[]
for i in range(m, n+1):
    s=str(i)
    tmp=[]
    for j in s:
        tmp.append(text[int(j)])
    arr.append([i, ' '.join(tmp)])
arr.sort(key=lambda x:x[1])
for i in range(len(arr)):
    if i%10==9:
        print(arr[i][0])
    else:
        print(arr[i][0], end=' ')