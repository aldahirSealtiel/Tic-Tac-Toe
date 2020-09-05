# put your python code here
numbers = input().split()
consult = input()


ans = []
count = 0
for number in numbers:
    if number == consult:
        ans.append(str(count))
    count += 1

if len(ans) > 0:
    print(" ".join(ans))
else:
    print("not found")
