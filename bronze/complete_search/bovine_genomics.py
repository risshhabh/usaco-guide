# https://usaco.org/index.php?page=viewproblem2&cpid=736

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("cownomics")

n_cows_2, len_genomes = splint()

spotty_pos = 0

spotted_per_gen = list(zip(*[input() for _ in range(n_cows_2)]))
plain = list(zip(*[input() for _ in range(n_cows_2)]))

for i in range(len_genomes):
    if set(spotted_per_gen[i]) & set(plain[i]):
        continue
    else:
        spotty_pos += 1

print(spotty_pos)