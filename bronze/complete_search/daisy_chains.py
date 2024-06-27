# https://usaco.org/index.php?page=viewproblem2&cpid=1060

splint = lambda : list(map(int, input().split()))

n_flowers = int(input())
petals = splint()

average_pictures = n_flowers

for i in range(2, n_flowers + 1):
    # scrolling window of length i
    for j in range(n_flowers - i + 1):
        win = petals[j:j + i]
        if sum(win) / i in win:
            average_pictures += 1

print(average_pictures)