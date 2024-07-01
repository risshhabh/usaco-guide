# https://usaco.org/index.php?page=viewproblem2&cpid=617

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("balancing")

n, b = splint()
points = [splint() for _ in range(n)]
M = 101

cur_a, cur_b = 0, 0

# for every point (r, s) in points, we shift all points (x, y) to (x - r - 1, y - s - 1).
# we then count the number of points in each quadrant after the shift.

def qshift(sgn1, sgn2):
    global M
    for point in points:
        r, s = point
        points_shifted = [(x - r + sgn1, y - s + sgn2) for x, y in points]

        q1, q2, q3, q4 = 0, 0, 0, 0

        for shifted_point in points_shifted:
            x, y = shifted_point

            if x >= 0 and y >= 0:
                q1 += 1
            elif x < 0 and y >= 0:
                q2 += 1
            elif x < 0 and y < 0:
                q3 += 1
            else:
                q4 += 1
        
        M = min(M, max(q1, q2, q3, q4))
    return 0

qshift(1, 1)
qshift(1, -1)
qshift(-1, 1)
qshift(-1, -1)

print(M)