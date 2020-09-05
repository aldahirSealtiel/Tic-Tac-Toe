numbers = [int(x) for x in input()]

ans = []
for i in range(1, len(numbers)):
    ans.append((numbers[i - 1] + numbers[i]) / 2)

print(ans)
