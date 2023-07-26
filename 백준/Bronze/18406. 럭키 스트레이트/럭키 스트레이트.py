s=list(map(int, input()))
if sum(s[0:len(s)//2])==sum(s[len(s)//2:]):
    print('LUCKY')
else:
    print('READY')