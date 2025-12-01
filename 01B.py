with open("test.txt") as f:
    instructions = [L.rstrip() for L in f.readlines()]

answer = 0
current_index = 50
for i in instructions:
    count = int(i[1:])
    if count >= 100:
        answer += count // 100
        count = int(i[-2:])

    if i.startswith("L"):
        if count > current_index:
            answer += 1
            current_index = abs(100 + (current_index - count))
        else:
            current_index = current_index - count

    else:
        if current_index + count > 99:
            answer += 1
            current_index = abs(100 - (current_index + count))
        else:
            current_index = current_index + count


print(answer)
