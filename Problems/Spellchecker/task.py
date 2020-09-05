dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()

ans = [x for x in words if x not in dictionary]

if len(ans) == 0:
    print("OK")
else:
    for word in ans:
        print(word)
