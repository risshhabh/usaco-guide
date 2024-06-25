def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("blist")

n_cows = int(input())

b_use = [0] * 1001

for _ in range(n_cows):
    s, t, b = splint()
    for i in range(s, t+1):
        b_use[i] += b

print(max(b_use))