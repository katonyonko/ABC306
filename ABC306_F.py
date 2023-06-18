import io
import sys
import pdb

_INPUT = """\
6
3 2
1 3
2 8
4 6
1 1
306
4 4
155374934 164163676 576823355 954291757
797829355 404011431 353195922 138996221
191890310 782177068 818008580 384836991
160449218 545531545 840594328 501899080
"""

class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    #合計にはrを含まない
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
    #pの位置をxという値にセット
    def set(self, p, x):
        self.add(p, -self.sum(p, p+1) + x)

def solve(test):
  N,M=map(int,input().split())
  bit=BIT(N*M)
  A=[list(map(int,input().split())) for _ in range(N)]
  tmp=[]
  for i in range(N): tmp+=A[i]
  tmp.sort()
  d={tmp[i]:i for i in range(N*M)}
  B=[[d[A[i][j]] for j in range(M)] for i in range(N)]
  ans=0
  for i in reversed(range(N)):
    for j in range(M):
      ans+=(N-1-i)*(j+1)+bit.sum(0,B[i][j])
    for j in range(M):
      bit.add(B[i][j],1)
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