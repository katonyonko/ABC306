import io
import sys
import pdb

_INPUT = """\
6
5
1 100
1 300
0 -200
1 500
1 300
4
0 -1
1 -2
0 -3
1 -4
15
1 900000000
0 600000000
1 -300000000
0 -700000000
1 200000000
1 300000000
0 -600000000
1 -900000000
1 600000000
1 -100000000
1 -400000000
0 900000000
0 200000000
1 -500000000
1 900000000
"""

def solve(test):
  N=int(input())
  x,y=0,0
  for i in range(N):
    X,Y=map(int,input().split())
    if X==0:
      if Y>=0:
        x=max(x+Y,y+Y)
      else:
        x=max(x,y+Y)
    else:
      if Y>=0:
        y=max(x+Y,y)
      else:
        y=max(x+Y,y)
  ans=max(x,y)
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)