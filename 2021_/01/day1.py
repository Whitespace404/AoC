depths = []

with open("day1.txt") as f:
    for line in f.readlines():
        depths.append(line.rstrip("\n"))

prev_depth = 149
counter = 0

for depth in depths:

    if int(depth) > int(prev_depth):
        counter += 1
        prev_depth = depth
    prev_depth = depth

print(f"The depth has increased {counter} times.")
