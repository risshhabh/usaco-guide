# https://usaco.org/index.php?page=viewproblem2&cpid=1011

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("triangles")

n_posts = int(input())
coords = [splint() for _ in range(n_posts)]

# we will test every coordinate as the vertex opposite to the hypotenuse
# see furthest A and B from C where A and B are on the same axes as C

max_area = 0
x, y = 0, 1

for C in coords:
    # furthest B
    B = max(filter(lambda b: b[x] == C[x], coords), key=lambda b: abs(b[y] - C[y]))
    # furthest A
    A = max(filter(lambda a: a[y] == C[y], coords), key=lambda a: abs(a[x] - C[x]))

    area = abs((B[y] - A[y]) * (C[x] - A[x]))
    max_area = max(max_area, area)

print(max_area)
