instructions = []

with open("day2.txt") as f:
    for line in f.readlines():
        instructions.append(line.rstrip("\n"))

def hide():
    horizontal_position = 0
    depth = 0
    aim = 0

    for instuction in instructions:
        if instuction.startswith("forward"):
            count = int(instuction.lstrip("forward "))
            horizontal_position += count
            depth += aim * count
        if instuction.startswith("down"):
            count = int(instuction.lstrip("down "))
            
            aim += count
        if instuction.startswith("up"):
            count = int(instuction.lstrip("up "))
            
            aim -= count
    return horizontal_position * depth

print(hide())
