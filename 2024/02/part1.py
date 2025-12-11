with open("input.txt") as f:
    lines = []
    for i in f.read().splitlines():
        lines.append(i)

answer = 0
for line in lines:
    L = line.split(" ")
    L = [int(i) for i in L]
    if all([L[i] > L[i + 1] for i in range(len(L) - 1)]) or all(
        [L[i] < L[i + 1] for i in range(len(L) - 1)]
    ):
        if all([abs(L[i + 1] - L[i]) <= 3 for i in range(len(L) - 1)]):
            answer += 1

print(answer)
