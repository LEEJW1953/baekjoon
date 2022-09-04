import sys
input=sys.stdin.readline

n, m = map(int, input().split())

s = []
def f(num):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(num, n + 1):
    s.append(i)
    f(i)
    s.pop()

f(1)