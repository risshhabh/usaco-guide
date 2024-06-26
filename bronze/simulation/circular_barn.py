# https://usaco.org/index.php?page=viewproblem2&cpid=616

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("cbarn")

dot_prod_vec = lambda N, occ : sum([n * occ_i for n, occ_i in zip(range(N), occ)])

N = int(input())
occ1 = [int(input()) for _ in range(N)]

from collections import deque
OCC_D = deque(occ1)

mins = []

for _ in range(N):
    mins.append(dot_prod_vec(N, OCC_D))
    OCC_D.rotate(1)

print(min(mins))