import sys
input=sys.stdin.readline

n=int(input())
s1, s2 = 0, 0
t1, t2 = 0, 0
time=0
for i in range(n):
    t, tmp = map(str, input().split())
    arr=tmp.split(':')
    nh, nm = int(arr[0]), int(arr[1])
    if t=='1':
        if s1+1==s2:
            hh=time//100
            mm=time%100
            time=nh*100+nm
            if nm<mm:
                nh-=1
                nm+=60
            ch, cm = t2//100+nh-hh, t2%100+nm-mm
            if 60<=cm:
                ch+=1
                cm-=60
            t2=ch*100+cm
        elif s1==s2:
            time=nh*100+nm
        s1+=1
    elif t=='2':
        if s2+1==s1:
            hh=time//100
            mm=time%100
            time=nh*100+nm
            if nm<mm:
                nh-=1
                nm+=60
            ch, cm = t1//100+nh-hh, t1%100+nm-mm
            if 60<=cm:
                ch+=1
                cm-=60
            t1=ch*100+cm
        elif s1==s2:
            time=nh*100+nm
        s2+=1
if s1<s2:
    nh, nm = 48, 0
    hh=time//100
    mm=time%100
    if nm<mm:
        nh-=1
        nm+=60
    ch, cm = t2//100+nh-hh, t2%100+nm-mm
    if 60<=cm:
        ch+=1
        cm-=60
    t2=ch*100+cm
elif s2<s1:
    nh, nm = 48, 0
    hh=time//100
    mm=time%100
    if nm<mm:
        nh-=1
        nm+=60
    ch, cm = t1//100+nh-hh, t1%100+nm-mm
    if 60<=cm:
        ch+=1
        cm-=60
    t1=ch*100+cm
print(f'{str(t1//100).zfill(2)}:{str(t1%100).zfill(2)}')
print(f'{str(t2//100).zfill(2)}:{str(t2%100).zfill(2)}')