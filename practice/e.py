amount = int(input().split()[1])

count = 0
for price in sorted(int(i) for i in input().split()):
    if amount >= price:
        count += 1
        amount -= price
        if amount == 0:
            break

print(count)
