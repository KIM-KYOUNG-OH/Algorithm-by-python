import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
answer = 0
candidates = []
for _ in range(m):
    package_price, individual_price = map(int, sys.stdin.readline().rstrip().split())
    candidates.append((package_price, individual_price))
candidates_order_by_package_price = sorted(candidates, key=lambda x: x[0])
min_package_price = candidates_order_by_package_price[0][0]
candidates_order_by_individual_price = sorted(candidates, key=lambda x: x[1])
min_individual_price = candidates_order_by_individual_price[0][1]

if min_package_price <= min_individual_price * 6:
    if min_package_price < min_individual_price * (n % 6):
        answer = min_package_price * ((n // 6) + 1)
    else:
        answer = min_package_price * (n // 6) + min_individual_price * (n % 6)
else:
    answer = min_individual_price * n
print(answer)