# https://usaco.org/index.php?page=viewproblem2&cpid=855

inp = [list(map(int, line.split())) for line in open("mixmilk.in", "r").read().splitlines()]
out = open("mixmilk.out", "w")

for i in range(100):
    from_, to_ = i % 3, (i + 1) % 3 # 0>1, 1>2, 2>0

    # * inp[from_] # c_X, m_X
    # * inp[to_]   # c_Y, m_Y

    mx = inp[from_][1]
    cY, mY = inp[to_]

    inp[from_][1], inp[to_][1] = 0 if (mx + mY <= cY) else (mx - (cY - mY)), min(cY, mx + mY)

for i in range(3):
    # print(inp[i][1])
    out.write(str(inp[i][1]) + "\n")
    out.close()