# https://usaco.org/index.php?page=viewproblem2&cpid=831

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("tttt")

board = [input() for _ in range(3)]
won = lambda l_w_s : [ j if len(j) < 3 else None for j in l_w_s ]
win_rows = won([frozenset(i) for i in board])
cols = won([frozenset(i) for i in zip(*board)])
diag_1 = won([frozenset([board[i][i  ] for i in range(3)])])
diag_2 = won([frozenset([board[i][2-i] for i in range(3)])])

set_win = set([i for i in win_rows + cols + diag_1 + diag_2 if i is not None])

print(sum([1 for i in set_win if len(i) == 1]))
print(sum([1 for i in set_win if len(i) == 2]))
