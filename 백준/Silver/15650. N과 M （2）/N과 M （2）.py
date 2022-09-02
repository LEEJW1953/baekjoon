import sys
input=sys.stdin.readline

n, m = map(int, input().split())

s = []
def f(num):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(num, n + 1):
    if i in s:
      continue
    s.append(i)
    f(i+1)
    s.pop()

f(1)