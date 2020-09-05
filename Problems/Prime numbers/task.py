prime_numbers = [x for x in range(2, 1001) if all(x % c for c in range(2, x))]

