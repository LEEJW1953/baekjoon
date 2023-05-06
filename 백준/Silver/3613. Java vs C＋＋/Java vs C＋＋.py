import sys
input=sys.stdin.readline

s=input().strip()
if s[0].isupper() or s[0]=='_':
    print('Error!')
    exit(0)
arr=s.split('_')
ans=''
if len(arr)==1:
    if arr[0].islower():
        print(arr[0])
    else:
        for i in arr[0]:
            if not i.isalpha():
                print('Error!')
                exit(0)
            if i.islower():
                ans+=i
            else:
                ans+='_'
                ans+=i.lower()
else:
    if not arr[0].islower():
        print('Error!')
        exit(0)
    for i in arr[0]:
        ans+=i
    for i in range(1, len(arr)):
        if not arr[i].islower():
            print('Error!')
            exit(0)
        for j in range(len(arr[i])):
            if not arr[i][j].isalpha():
                print('Error!')
                exit(0)
            if j==0:
                ans+=arr[i][j].upper()
            else:
                ans+=arr[i][j]
print(ans)