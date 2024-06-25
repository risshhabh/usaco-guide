# https://usaco.org/index.php?page=viewproblem2&cpid=664 

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))


old_contest("blocks")

n_cards = int(input())
cards = [input().split() for _ in range(n_cards)]


from collections import Counter

st = "abcdefghijklmnopqrstuvwxyz"

for letter in st:
    for card in cards:
        st += letter * (max(card[0].count(letter), card[1].count(letter)))


occ = Counter(st)
get_out = lambda counter_ : [i-1 for i in list(counter_.values())]

for i in get_out(occ):
    print(i)