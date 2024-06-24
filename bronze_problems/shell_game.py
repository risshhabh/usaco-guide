# https://usaco.org/index.php?page=viewproblem2&cpid=891

inp = [list(map(int, line.split())) for line in open("shell.in", "r").read().splitlines()]
out = open("shell.out", "w")

n_swaps = inp[0][0]
max_correct_guesses = 0
correct_guesses = []

for start_pos in range(3): # start_pos is the shell that the ball starts in
    shells = [0, 0, 0] # empty shells = 0
    shells[start_pos] = 1 # this is the rock
    
    for swap in range(n_swaps):
        a, b, g = inp[swap + 1]
        shells[a - 1], shells[b - 1] = shells[b - 1], shells[a - 1]
        max_correct_guesses += shells[g - 1]
    correct_guesses.append(max_correct_guesses)
    max_correct_guesses = 0

# print(max(correct_guesses))
out.write(str(max(correct_guesses)))