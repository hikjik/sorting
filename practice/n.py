n = int(input())
inp = [[int(i) for i in input().split()] for _ in range(n)]

res = []
for cur in sorted(inp):
    if res and res[-1][1] >= cur[0]:
        res[-1][1] = max(res[-1][1], cur[1])
    else:
        res.append(cur)

for r in res:
    print(*r)
