def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("pails")

X, Y, M = splint()

all_X = list(range(X, M, X))
all_XY = [((M - i) // Y) * Y + i for i in all_X]


print(max(all_XY))
