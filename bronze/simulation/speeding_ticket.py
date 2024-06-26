# https://usaco.org/index.php?page=viewproblem2&cpid=568

def old_contest(filename_no_ext):
    import sys

    sys.stdin = open(filename_no_ext + ".in", "r")
    sys.stdout = open(filename_no_ext + ".out", "w")

    return

splint = lambda : list(map(int, input().split()))

old_contest("speeding")

road_segments, bessie_segments = splint()

road_segments_limits = [splint() for _ in range(road_segments)]
bessie_segments_limits = [splint() for _ in range(bessie_segments)]


per_mile_road_limits = [([segment[1]] * segment[0]) for segment in road_segments_limits]
per_mile_bessie_limits = [[segment[1]] * segment[0] for segment in bessie_segments_limits]

road_miles = []
for seg in per_mile_road_limits:
    road_miles.extend(seg)
bessie_miles = []
for seg in per_mile_bessie_limits:
    bessie_miles.extend(seg)


print(max(0,
    max(map(int.__sub__, bessie_miles, road_miles))
))