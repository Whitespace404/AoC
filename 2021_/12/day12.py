path = []
print()
with open("day12.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        path.append(line.rstrip("\n"))

start = []
end = []

for p in path:
    if "start" in p:
        start.append(p)
    elif "end" in p:
        end.append(p)

print(f"Start: {start}")
print(f"End:   {end}")
print()
