import sys

while True:
    s=sys.stdin.readline().rstrip()
    arr=[]
    result=True
    if s=='.':
        break
    for i in s:
        if i=='(' or i=='[':
            arr.append(i)
        elif i==')':
            if not arr or arr[-1]=='[':
                result=False
                break
            elif arr[-1]=='(':
                arr.pop()
        elif i==']':
            if not arr or arr[-1]=='(':
                result=False
                break
            elif arr[-1]=='[':
                arr.pop()
    if result==True and not arr:
        print('yes')
    else:
        print('no')