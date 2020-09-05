matches = int(input())
ans = list()
wins = 0
for _ in range(matches):
    data = input().split()
    if data[1] == "win":
        ans.append(data[0])
        wins += 1

print(ans)
print(wins)