# https://cses.fi/problemset/task/2165

time = 0
def hanoi(i, p, o, n):
    global time
    if n == 1:
        print(i, o)
        time += 1
    else:
        hanoi(i, o, p, n - 1)
        hanoi(i, p, o, 1)
        hanoi(p, i, o, n - 1)

n = int(input())
print((1 << n) - 1) # 2 ** n - 1 moves
hanoi(1, 2, 3, n)