# https://usaco.org/index.php?page=viewproblem2&cpid=784

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("lifeguards")

n_guards = int(input())
shifts = [splint() for _ in range(n_guards)]
shifts = [range(x, y) for x, y in shifts]

max_time = 0
for guard in shifts:
    times_covered = set()
    for shift in shifts:
        times_covered.update(shift if shift != guard else [])
    
    print(times_covered)
    max_time = max(max_time, len(times_covered))

print(max_time)