hour, min = map(int, input().split())
if min<45:
    if hour==0:
        print(hour+23, min+15)
    else:
        print(hour-1, min+15)
else:
    print(hour, min-45)