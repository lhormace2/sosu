def infinite_primes():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1

# 無限の素数ジェネレータを作成
primes = infinite_primes()

# 最初の100000個の素数を表示
for _ in range(100000):
    print(next(primes))