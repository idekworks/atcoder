R, C = map(int, input().split())

data = [[[-1] for _ in range(C + 1)] for _ in range(R + 1)]

for r in range(R):
    row = list(map(int, input().split()))
    sum_row = sum(row)
    row.append(sum_row)
    data[r] = row
for c in range(C + 1):
    sum = 0
    for r in range(R):
        sum += data[r][c]
    data[R][c] = sum

for r in range(R + 1):
    print(" ".join(map(str, data[r])))