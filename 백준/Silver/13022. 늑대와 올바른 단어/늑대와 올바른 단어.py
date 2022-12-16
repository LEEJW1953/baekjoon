s=input().strip()
if len(s)%4!=0:
    print(0)
else:
    w, o, l, f = 0, 0, 0, 0
    for i in range(len(s)):
        if i==0 and s[i]!='w':
            print(0)
            exit(0)
        if s[i]=='w':
            if i>=1 and s[i-1]!='w':
                if s[i-1]=='f':
                    if w==o==l==f:
                        w=1
                    else:
                        print(0)
                        exit(0)
                else:
                    print(0)
                    exit(0)
            else:
                w+=1
        elif s[i]=='o':
            if i>=1 and s[i-1]!='o':
                if s[i-1]=='w':
                    o=1
                else:
                    print(0)
                    exit(0)
            else:
                o+=1
        elif s[i]=='l':
            if i>=1 and s[i-1]!='l':
                if s[i-1]=='o':
                    l=1
                else:
                    print(0)
                    exit(0)
            else:
                l+=1
        elif s[i]=='f':
            if i>=1 and s[i-1]!='f':
                if s[i-1]=='l':
                    f=1
                else:
                    print(0)
                    exit(0)
            else:
                f+=1
    if w==o==l==f:
        print(1)
    else:
        print(0)