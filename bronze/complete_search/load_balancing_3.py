# https://usaco.org/index.php?page=viewproblem2&cpid=617

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("balancing")

n, b = splint()
xpos, ypos = [], []
for i in range(n):
    x, y = splint()
    xpos.append(x)
    ypos.append(y)
M = 101

def qshift(sgn1, sgn2):
    global M
    for X in xpos:
        for Y in ypos:
            q1, q2, q3, q4 = 0, 0, 0, 0
            X += sgn1
            Y += sgn2

            for x, y in zip(xpos, ypos):
                if x > X and y > Y:
                    q1 += 1
                elif x < X and y > Y:
                    q2 += 1
                elif x < X and y < Y:
                    q3 += 1
                else:
                    q4 += 1
                
            M = min(M, max(q1, q2, q3, q4))
    return 0

qshift(1, 1)
qshift(-1, 1)
qshift(1, -1)
qshift(-1, -1)

print(M)