def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("badmilk")

n_friends, n_milk_types, n_drinks, n_sick = splint()

# person_ix, milk_type, time
drinks = [splint() for _ in range(n_drinks)]
# person_ix who got sick
sick = set(splint()[0] for _ in range(n_sick))

drank = {}
for person_ix, milk_type, time in drinks:
    if milk_type not in drank:
        drank[milk_type] = set()
    drank[milk_type].add(person_ix)

cures = set()
for dranks in drank.values():
    if sick.issubset(dranks):
        cures.update(dranks)

print(len(cures))

# issue with this solution is that it doesn't account for the time the person got sick
# so it's possible that a person drank the contaminated milk after the person got sick