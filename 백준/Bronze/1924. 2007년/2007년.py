import sys
input=sys.stdin.readline

date={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
day={0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}
x, y = map(int, input().split())
n=0
for i in range(1, x):
    n+=date[i]
n+=y
print(day[n%7])