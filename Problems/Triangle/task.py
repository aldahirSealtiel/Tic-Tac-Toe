height = int(input())

for i in range(1, height + 1):
    print("".join(" " for i in range(height - i)) + "".join("#" for i in range(2 * i - 1)))
