s=list(input())
if s[0]=='F':
    print(0.0)
else:
    ans=4-(ord(s[0])-65)
    if s[1]=='-':
        ans-=0.3
    elif s[1]=='+':
        ans+=0.3
    else:
        ans=float(ans)
    print(ans)