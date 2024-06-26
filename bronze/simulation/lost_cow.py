def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("lostcow")

d_trav = 0

x, y = splint()
sgn_dist = y - x
fj = x

n = 0
while ((fj < y) if sgn_dist > 0 else (fj > y)):
    d_trav += abs((x + (-2) ** n) - (fj))
    fj = x + (-2) ** n
    n += 1
d_trav -= abs(fj - y)

print(d_trav)