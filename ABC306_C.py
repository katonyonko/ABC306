import io
import sys
import pdb

_INPUT = """\
6
3
1 1 3 2 3 2 2 3 1
1
1 1 1
4
2 3 4 3 4 1 3 1 1 4 2 2
"""

def solve(test):
  N=int(input())
  A=list(map(lambda x:int(x)-1,input().split()))
  cnt=[0]*N
  f=[-1]*N
  for i in range(3*N):
    if cnt[A[i]]==1: f[A[i]]=i
    cnt[A[i]]+=1
  ans=sorted([(f[i],i+1) for i in range(N)])
  if test==0:
    print(*[ans[i][1] for i in range(N)])
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