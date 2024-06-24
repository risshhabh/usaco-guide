# https://usaco.org/index.php?page=viewproblem2&cpid=665

inp = open("cowsignal.in", "r")
out = open("cowsignal.out", "w")

m, n, k = list(map(int, inp.readline().split()))

# m by n matrix amplified k times

signal = inp.read()
# first horiz stretch
signal_amp_width = signal.replace("X", "X" * k).replace(".", "." * k).splitlines()

# then vert stretch
for line in signal_amp_width:
    out.write((line + "\n") * k)
    # print((line + "\n") * k, end="")
out.close()