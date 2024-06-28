# https://usaco.org/index.php?page=viewproblem2&cpid=712

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("circlecross")

inp = input()
get_ind_pair = lambda letter: (inp.index(letter), inp.rindex(letter))


def crossover(a, b):
    A = get_ind_pair(a)
    B = get_ind_pair(b)

    if A[0] < B[0] < A[1] < B[1] or B[0] < A[0] < B[1] < A[1]:
        return True
    return False

print(
    sum(
        crossover(a, b)
        for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if a < b
    )
)