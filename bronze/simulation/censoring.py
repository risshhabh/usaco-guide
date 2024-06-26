# https://usaco.org/index.php?page=viewproblem2&cpid=526

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("censor")

S = input()
T = input()

while T in S:
    S = S.replace(T, '', 1)

print(S)