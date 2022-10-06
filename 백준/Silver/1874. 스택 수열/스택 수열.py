n=int(input())
arr=[]
arr1=[]
num=1
result=True
for i in range(n):
    a=int(input())
    while num<=a:
        arr.append(num)
        arr1.append('+')
        num+=1
    if arr[-1]==a:
        arr.pop()
        arr1.append('-')
    else:
        print('NO')
        result=False
        break
if result:
    for i in range(len(arr1)):
        print(arr1[i])