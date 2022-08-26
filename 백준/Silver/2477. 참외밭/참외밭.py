k=int(input())
arr=[]
width=[]
height=[]
for i in range(6):
    dir, len=map(int,input().split())
    if dir==1 or dir==2:
        width.append(len)
        arr.append(len)
    elif dir==3 or dir==4:
        height.append(len)
        arr.append(len)
xx=max(width)
yy=max(height)
a=arr.index(max(height))
b=arr.index(max(width))
if a==0:
    xi=5
    xj=1
elif a==5:
    xi=4
    xj=0
else:
    xi=a-1
    xj=a+1
if b==0:
    yi=5
    yj=1
elif b==5:
    yi=4
    yj=0
else:
    yi=b-1
    yj=b+1
width.remove(arr[xi])
width.remove(arr[xj])
height.remove(arr[yi])
height.remove(arr[yj])
s=width[0]*height[0]
print(k*((xx*yy)-s))