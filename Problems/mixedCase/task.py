words = input().split()
ans = []
count = 0
for word in words:
    if count == 0:
        ans.append(word)
    else:
        ans.append(word.capitalize())
    count += 1
print("".join(ans))
