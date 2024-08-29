n, k = 25, 3
count = 0

while True:
    if n == 1 :
        print(count)
    if n % k == 0:
        n //= k
        count += 1
        continue
    else:
        n -= 1
        count += 1
        continue
    