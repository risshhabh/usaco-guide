def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("gymnastics")

k, n = splint()
orders = [splint() for _ in range(k)]

count = 0

for i in range(1, n+1):
    for j in range(i+1, n+1):
        a = 0
        for order in orders:
            if order.index(i) > order.index(j):
                a += 1
            else:
                a -= 1
        if abs(a) == k:
            count += 1

print(count)
