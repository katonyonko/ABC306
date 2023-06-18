import io
import sys
from heapq import heappush, heappop
from collections import defaultdict

_INPUT = """\
6
4 2 10
1 5
2 1
3 3
4 2
2 10
1 0
4 0
3 1
2 0
3 0
"""

def solve(test):
  N,K,Q=map(int,input().split())
  d1,d2=defaultdict(int),defaultdict(int)
  d1[0]=K
  d2[0]=N-K
  A=[0]*N
  h1,h2=[],[]
  for i in range(K):
    heappush(h1,0)
  for i in range(N-K):
    heappush(h2,0)
  ans=0
  for i in range(Q):
    X,Y=map(int,input().split())
    X-=1
    a,b=A[X],Y
    A[X]=Y
    if d1[a]>0:
      d1[a]-=1
      heappush(h2,-Y)
      d2[Y]+=1
      while d2[-h2[0]]==0: heappop(h2)
      z=-heappop(h2)
      d2[z]-=1
      heappush(h1,z)
      d1[z]+=1
      ans+=-a+z
    else:
      d2[a]-=1
      heappush(h1,Y)
      d1[Y]+=1
      while d1[h1[0]]==0: heappop(h1)
      z=heappop(h1)
      d1[z]-=1
      heappush(h2,-z)
      d2[z]+=1
      ans+=Y-z
    # print(h1,d1,h2,d2)
    print(ans)

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