n=int(input())
for i in range(n):
    str=''
    for _ in range(n-1-i):
        str+=' '
    for _ in range(2*(i+1)-1):
        str+='*'
    print(str)