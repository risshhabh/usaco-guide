splint = lambda : list(map(int, input().split()))

def add_elements(lst, i):
    return lst[:i] + [lst[i] + lst[i+1]] + lst[i+2:]

def add_elements_2(lst, i, ii1):
    # ii1: int = lst[i] + lst[i+1]
    return lst[:i] + [ii1] + lst[i+2:]

for _ in range(int(input())):
    n_pers = int(input())
    times_sleep = splint()
    times_sleep_original = times_sleep[:]
    total_sleep = sum(times_sleep)

    sleep_aim = max(times_sleep)
    at = 0

    while len(set(times_sleep)) != 1:
        
        # check if aim is achievable
        if total_sleep % sleep_aim != 0:
            sleep_aim += 1
            at = 0
            times_sleep = times_sleep_original[:]
            continue

        # check if at is at sleep_aim
        if times_sleep[at] == sleep_aim:
            at += 1
            continue
        
        # check if add_elements_2 is possible
        ii1 = times_sleep[at] + times_sleep[at+1]
        if ii1 > sleep_aim:
            sleep_aim += 1
            at = 0
            times_sleep = times_sleep_original[:]
            continue

        times_sleep = add_elements_2(times_sleep, at, ii1)

    print(n_pers - len(times_sleep)) # joins = len_i - len_f