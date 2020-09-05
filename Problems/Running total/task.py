numbers = [int(x) for x in input()]
ans = [sum(numbers[:x + 1]) for x in range(len(numbers))]
print(ans)