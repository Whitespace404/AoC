with open("01.txt") as f:
    instructions = [L.rstrip() for L in f.readlines()]


def traverse_left(current_index, count):
    Delta = current_index - count
    return Delta if Delta >= 0 else abs(100 + Delta)


def traverse_right(current_index, count):
    Delta = current_index + count
    return Delta if Delta <= 99 else abs(100 - Delta)


current_index = 50
count = 0
for i in instructions:
    c = int(i[1:])
    if c >= 100:
        c = int(i[-2:])
    if i.startswith("L"):
        current_index = traverse_left(current_index, c)
    else:
        current_index = traverse_right(current_index, c)
    if current_index == 0:
        count += 1
print(count)
