a, b=map(int, input().split())
c=int(input())
hour = a + (c//60)
min = b + (c%60)
if min<=59:
    if hour<=23:
        print(hour, min)
    else:
        print(hour-24, min)
else:
    if hour<=22:
        print(hour+1, min-60)
    else:
        print(hour-23, min-60)