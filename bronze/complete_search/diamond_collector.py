# https://usaco.org/index.php?page=viewproblem2&cpid=639

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("diamond")


N, K = splint()
sizes = [int(input()) for _ in range(N)]
max_dia = 0

for s in sizes:
    n_dia = sum(1 for i in sizes if s <= i <= s + K)
    max_dia = max(max_dia, n_dia)

print(max_dia)